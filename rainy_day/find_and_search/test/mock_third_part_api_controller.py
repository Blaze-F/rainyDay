import datetime
from typing import List

from exceptions import NotFoundError


class MockApiController:
    """테스트 코드용 Mock 객체"""

    def __init__(self) -> None:
        pass

    def request_drain_pipe_water_level(
        district_name: str,
        start_ymdh=(datetime.datetime.now() - datetime.timedelta(hours=1)).strftime("%Y%m%d%H"),
        end_ymdh=datetime.datetime.now().strftime("%Y%m%d%H"),
        row=1,
    ) -> List[dict]:
        """
        테스트 코드용 Mock 메서드
        """
        res = [
            {
                "IDN": "04-0011",
                "GUBN": "04",
                "GUBN_NAM": "성동",
                "MEA_YMD": "2022-11-10 17:00:00.0",
                "MEA_WAL": 0.04,
                "SIG_STA": "통신양호",
                "REMARK": "서울특별시 성동구 행당로17길 26 ...공 정문 앞 도로변",
            }
        ]

        try:
            return res
        except:
            raise NotFoundError

    def request_list_rainfall_amount(
        district_name: str,
        row_amount: int,
    ) -> List[dict]:
        """
        테스트 코드용 Mock 메서드
        """
        data = {
            "ListRainfallService": {
                "list_total_count": 278212,
                "RESULT": {"CODE": "INFO-000", "MESSAGE": "정상 처리되었습니다"},
                "row": [
                    {
                        "RAINGAUGE_CODE": 101,
                        "RAINGAUGE_NAME": "강남구청",
                        "GU_CODE": 101,
                        "GU_NAME": "강남구",
                        "RAINFALL10": 0,
                        "RECEIVE_TIME": "2022-11-10 15:19",
                    },
                    {
                        "RAINGAUGE_CODE": 102,
                        "RAINGAUGE_NAME": "세곡동",
                        "GU_CODE": 101,
                        "GU_NAME": "강남구",
                        "RAINFALL10": 0,
                        "RECEIVE_TIME": "2022-11-10 15:19",
                    },
                    {
                        "RAINGAUGE_CODE": 103,
                        "RAINGAUGE_NAME": "개포2동",
                        "GU_CODE": 101,
                        "GU_NAME": "강남구",
                        "RAINFALL10": 0,
                        "RECEIVE_TIME": "2022-11-10 15:19",
                    },
                    {
                        "RAINGAUGE_CODE": 201,
                        "RAINGAUGE_NAME": "강동구청",
                        "GU_CODE": 102,
                        "GU_NAME": "강동구",
                        "RAINFALL10": 0,
                        "RECEIVE_TIME": "2022-11-10 15:19",
                    },
                    {
                        "RAINGAUGE_CODE": 202,
                        "RAINGAUGE_NAME": "고덕2동",
                        "GU_CODE": 102,
                        "GU_NAME": "강동구",
                        "RAINFALL10": 0,
                        "RECEIVE_TIME": "2022-11-10 15:19",
                    },
                ],
            }
        }
        try:
            return data
        except:
            raise NotFoundError


class MockApiControllerRaiseError:
    """무조건 NotFoundError를 발생시키는 Mock Controller 입니다."""

    def __init__(self) -> None:

        pass

    def request_drain_pipe_water_level(
        self,
        district_name: str,
        start_ymdh=(datetime.datetime.now() - datetime.timedelta(hours=1)).strftime("%Y%m%d%H"),
        end_ymdh=datetime.datetime.now().strftime("%Y%m%d%H"),
        row=1,
    ) -> List[dict]:

        raise NotFoundError

    def request_list_rainfall_amount(
        self,
        district_name: str,
        row_amount: int,
    ) -> List[dict]:

        raise NotFoundError
