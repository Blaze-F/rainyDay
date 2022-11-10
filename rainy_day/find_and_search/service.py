import datetime
from typing import List
from config.config import Config
from find_and_search.serializer import findAndSearchResSchema


class FindAndSearchService:
    def __init__(self, api_controller) -> None:
        self.api_controller = api_controller

    def get_amount_of_gauge(self, district_name: str) -> int:
        """3개의 sample row를 요청하여 강우량계 갯수를 산출해냅니다. cf.중구는 예외"""
        if district_name == "중구":  # 중구의 경우는 강우량계 코드 규칙을 따르지 않으므로 예외처리함.
            return 2
        else:
            data = self.api_controller.request_list_rainfall_amount(
                district_name=district_name, row_amount=3
            )

        # result = data.pop("RESULT")
        codes = []
        for row in data["ListRainfallService"]["row"]:
            codes.append(int(row["RAINGAUGE_CODE"]) % 100)

        amount_of_gauge = max(codes)

        return amount_of_gauge

    def get_avg_of_rainflalls_in_day(self, district_name: str, amount_of_gauge: int) -> float:
        """강우량계 개수 * 하루치(상수 : config에 있음) 만큼의 요청을 보내어서 평균을 산출"""
        DAY_DIVIDE_BY_I0_MIN = Config.DAY_DIVIDE_BY_10_MIN  # defalut : 144

        data = self.api_controller.request_list_rainfall_amount(
            district_name=district_name, row_amount=amount_of_gauge * DAY_DIVIDE_BY_I0_MIN
        )
        summary = 0
        for row in data["ListRainfallService"]["row"]:
            summary += int(row["RAINFALL10"])

        avg = summary / amount_of_gauge

        return avg

    def request_water_level_and_day_avg_rainfall(
        self,
        district_name: str,
    ) -> List[dict]:
        """현재 수위와 24시간 누적 강수량을 리턴합니다. 외부 요청은 하수관로에 한번 강수량에 두번 보내집니다."""

        drain_pipe_levels_list = self.api_controller.request_drain_pipe_water_level(
            district_name=district_name
        )
        drain_pipe_levels = drain_pipe_levels_list.pop()
        amount_of_gauge = self.get_amount_of_gauge(district_name=district_name)
        rainfall_amount_in_day_avg = self.get_avg_of_rainflalls_in_day(
            district_name=district_name, amount_of_gauge=amount_of_gauge
        )

        data = {
            "district": drain_pipe_levels["GUBN_NAM"] + "구",
            "district_code": drain_pipe_levels["GUBN"],
            "drain_pipe_water_level": drain_pipe_levels["MEA_WAL"],
            "measure_ymd": drain_pipe_levels["MEA_YMD"],
            "total_rainfalls_in_day": rainfall_amount_in_day_avg,
            "summary_ymd": datetime.datetime.now().strftime("%Y.%m.%d - %H"),
        }

        res = findAndSearchResSchema(data=data)
        res.is_valid(raise_exception=True)
        return res.data
