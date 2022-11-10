from django.conf import settings
import pytest
from exceptions import NotFoundError


from find_and_search.service import FindAndSearchService
from find_and_search.test.mock_third_part_api_controller import (
    MockApiController,
    MockApiControllerRaiseError,
)


class TestService:
    @classmethod
    def setup_class(self):
        # Mock 객체 주입
        self.controller = MockApiController
        self.service = FindAndSearchService(api_controller=self.controller)

    @classmethod
    def teardown_class(self):
        pass

    def test_get_amount_of_gauge(self) -> int:
        # given
        district_name = "성동구"
        # when
        res = self.service.get_amount_of_gauge(district_name=district_name)
        # then
        assert isinstance(res, int)

    def test_get_avg_of_rainflalls_in_day(self):
        # given
        district_name = "강남구"
        # when
        res = self.service.get_avg_of_rainflalls_in_day(
            district_name=district_name, amount_of_gauge=2
        )
        # then
        assert isinstance(res, float)

    def test_request_water_level_and_day_avg_rainfall(self):
        # given
        district_name = "강남구"
        # when
        res = self.service.request_water_level_and_day_avg_rainfall(district_name=district_name)
        # then
        assert isinstance(res, dict)


class TestServiceErrorHandle:
    """NotFoundError 핸들링"""

    @classmethod
    def setup_class(self):
        # Mock 객체 주입
        self.controller = MockApiControllerRaiseError()
        self.service = FindAndSearchService(api_controller=self.controller)

    @classmethod
    def teardown_class(self):
        pass

    def test_request_water_level_and_day_avg_rainfall(self):

        # given
        district_name = "성동구"
        # when, #then
        with pytest.raises(NotFoundError):
            res = self.service.get_amount_of_gauge(district_name=district_name)

    def test_error_handle_amount_of_gauge(self):

        # given
        district_name = "강남구"
        # when, #then
        with pytest.raises(NotFoundError):
            res = self.service.get_avg_of_rainflalls_in_day(
                district_name=district_name, amount_of_gauge=2
            )

    def test_error_handle_request_water_level_and_day_avg_rainfall(self):

        # given
        district_name = "강남구"
        # when, #then
        with pytest.raises(NotFoundError):
            res = self.service.request_water_level_and_day_avg_rainfall(district_name=district_name)
