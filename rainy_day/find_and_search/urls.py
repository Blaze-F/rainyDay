from django.urls import path

from find_and_search.controller import live_data_get, live_data_get_for_user






app_name = "find_and_search"
urlpatterns = [
    path("get/", live_data_get, name="get_level_rain_avg"),
    path("getuser/", live_data_get_for_user, name="get_level_rain_avg_user"),
]
