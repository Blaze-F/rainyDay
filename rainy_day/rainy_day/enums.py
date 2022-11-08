from enum import Enum
from enum import auto
from rainy_day.rainy_day.enums import BaseEnum

class BaseEnum(Enum):
    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class DistrictInSeoul(BaseEnum): 
    """회원가입시, 검색시 사용하는 지역 열거"""
    종로구 = auto()
    중구 = auto()
    용산구 = auto()
    성동구 = auto()
    광진구 = auto()
    동대문구 = auto()
    중랑구 = auto()
    성북구 = auto()
    강북구 = auto()
    도봉구 = auto()
    노원구 = auto()
    은평구 = auto()
    서대문구 = auto()
    마포구 = auto()
    양천구 = auto()
    강서구 = auto()
    구로구 = auto()
    금천구 = auto()
    영등포구 = auto()
    동작구 = auto()
    관악구 = auto()
    서초구 = auto()
    강남구 = auto()
    송파구 = auto()
    강동구 = auto()
