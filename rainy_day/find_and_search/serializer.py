
from rest_framework import serializers


    
class findAndSearchResSchema(serializers.Serializer):
    """검색에 대한 응답 정의입니다."""
    district = serializers.CharField(max_length=5)
    district_code = serializers.CharField()
    drain_pipe_water_level = serializers.FloatField()
    measure_ymd = serializers.CharField()
    total_rainfalls_in_day = serializers.IntegerField()
    summary_ymd = serializers.CharField()