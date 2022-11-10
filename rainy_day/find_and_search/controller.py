from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from decorator.auth_handler import must_be_user
from decorator.execption_handler import execption_hanlder
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Parameter, IN_QUERY

from find_and_search.service import FindAndSearchService
from find_and_search.third_api_controller import ThirdApiController

third_party_api_controller = ThirdApiController()
find_and_search_service = FindAndSearchService(third_party_api_controller)


@swagger_auto_schema(
    method="get",
    manual_parameters=[
        Parameter("district_name", IN_QUERY, "검색 지역 입니다. 쿼리스트링입니다.", type="str"),
    ],
)
@api_view(["GET"])
@execption_hanlder()
@parser_classes([JSONParser])
def live_data_get(request):

    district_name = request.GET["district_name"]
    res = find_and_search_service.request_water_level_and_day_avg_rainfall(
        district_name=district_name
    )

    return JsonResponse(res, status=200, safe=False)


@swagger_auto_schema(method="get")
@api_view(["GET"])
@execption_hanlder()
@must_be_user()
@parser_classes([JSONParser])
def live_data_get_for_user(request):

    location = request.user["location"]
    res = find_and_search_service.request_water_level_and_day_avg_rainfall(district_name=location)

    return JsonResponse(res, status=200, safe=False)
