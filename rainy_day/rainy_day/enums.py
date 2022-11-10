from enum import Enum, unique

class BaseEnum(Enum):
    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

@unique
class DistrictInSeoul(BaseEnum): 
    """회원가입시, 검색시 사용하는 지역 열거, 구분명, 구분코드 순서입니다."""
    종로구 = 1
    중구 = 	2
    용산구 = 3
    성동구 = 4
    광진구 = 5
    동대문구 = 6
    중랑구 = 7
    성북구 = 8
    강북구 = 9
    도봉구 = 10
    노원구 = 11
    은평구 = 12
    서대문구 = 13
    마포구 = 14
    양천구 = 15
    강서구 = 16
    구로구 = 17
    금천구 = 18
    영등포구 = 19
    동작구 = 20
    관악구 = 21
    서초구 = 22
    강남구 = 23
    송파구 = 24
    강동구 = 25




