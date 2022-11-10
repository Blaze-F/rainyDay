
"""
    http://openapi.seoul.go.kr:8088/(인증키)/json/ListRainfallService/1(start_row)/5(end_row)/강남구
    http://openapi.seoul.go.kr:8088/(인증키)/json/서비스명/start_row/end_row/GUBN(int,코드)/YYYYMMDDHH(시작시간)/YYYYMMDDHH(종료시간)
    """
    

""" 서울시 OPEN API 요청관리"""
    

import datetime
import json
from typing import List

import requests

from config.config import Config
from exceptions import NotFoundError
from rainy_day.enums import DistrictInSeoul





class ThirdApiController():
    def __init__(self) -> None:
        self.auth_key = Config.open_api_key
        self.district_enum = DistrictInSeoul

    def request_drain_pipe_water_level(
        self,
        district_name: str,
        start_ymdh = (datetime.datetime.now() - datetime.timedelta(hours=1)).strftime("%Y%m%d%H"),
        end_ymdh = datetime.datetime.now().strftime("%Y%m%d%H"),
        row = 1
    ) -> List[dict]:
        """
        서울시 하수관로 수위 현황 데이터 요청 후 응답. 날짜는 YYYYMMDDHH 형태의 요청입니다. default row  1 , start : now -1h, end : now
        """
        
        district_code = self.district_enum[f"{district_name}"].value
        district_code_str = str(district_code)
        district_code_str = district_code_str.zfill(2)
        self.drain_pipe_monitoring_info_url = f"http://openAPI.seoul.go.kr:8088/{self.auth_key}/json/DrainpipeMonitoringInfo/1/{row}/{district_code_str}/{start_ymdh}/{end_ymdh}"
        response = requests.get(self.drain_pipe_monitoring_info_url)
        result = json.loads((response.content).decode("utf-8"))
        try : 
            return result["DrainpipeMonitoringInfo"]["row"]
        except :
            raise NotFoundError

    def request_list_rainfall_amount(
        self,
        district_name: str,
        row_amount: int,
    ) -> List[dict]:
        """
        서울시 구 강우량계 강수량 정보 응답.
        """
        self.list_rainfall_service_url = f"http://openAPI.seoul.go.kr:8088/{self.auth_key}/json/ListRainfallService/1/{row_amount}/{district_name}"
        response = requests.get(self.list_rainfall_service_url)
        result = json.loads((response.content).decode("utf-8"))
        return result

    
