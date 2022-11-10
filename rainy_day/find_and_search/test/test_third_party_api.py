from django.test import TestCase

from find_and_search.third_api_controller import ThirdApiController
from rainy_day.enums import DistrictInSeoul


class ThirdApiTest(TestCase):
    """서울시 api 실제 요청과 응답을 테스트합니다. 본 테스트 파일은 격리되어있지 않습니다."""

    def setUp(self) -> None:
        self.third_api_controller = ThirdApiController()

    def test_drain_pipe_water_level(self):
        # given
        input = "성동구"
        # when
        res = self.third_api_controller.request_drain_pipe_water_level(district_name=input)
        # then
        assert type(res) == list

    def test_rainfall_request(self):
        # given
        input = "성동구"
        # when
        res = self.third_api_controller.request_list_rainfall_amount(
            district_name=input, row_amount=1
        )
        # then
        assert type(res) == dict
