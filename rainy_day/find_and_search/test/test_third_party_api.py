from django.test import TestCase

from find_and_search.third_api_controller import ThirdApiController
from rainy_day.enums import DistrictInSeoul


class ThirdApiTest(TestCase):
    def setUp(self) -> None:
        self.third_api_controller = ThirdApiController()

    def test_drain_pipe_water_level(self):
        # given
        input = "성동구"
        # when
        res = self.third_api_controller.request_drain_pipe_water_level(district_name=input)
        # then
        assert type(res) == list
