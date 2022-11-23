# rainyDay
강수량과 하천 수위에 관한 API 입니다.

## Install

```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python -m manage.py runserver
```


## TestCoverage
2022-11-10 현재 91.6%입니다.
![image](https://user-images.githubusercontent.com/101803254/201149263-db04eda1-fed1-47a5-b164-0659c4c20f8b.png)

확인방법
```
pytest --cov
```

## Documentation


본 프로젝트는 스웨거를 이용하여, 문서화 하였습니다.

![image](https://user-images.githubusercontent.com/101803254/201134034-728dfa13-c6b7-45d3-aeeb-9d2a04f6a8f3.png)


서버 실행 후

{host_url}/swagger 로 들어가시면, 문서를 확인할 수 있습니다.

### GET 의 경우 쿼리 파라미터로 받습니다.



프로젝트 내 config.config_example.yml 참고해서 config.yml 작성해주세요. 

```yaml
databases:
  host: "localhost"
  port: 3306
  database: "rainy_day"
  username: "db user name"
  password: "db pw"
  timezone: "+09:00"

secrets:
  django: "django secret"

token:
  scret: "jwt secret"
  expire_sec: 3600

seoul_open_api_key: ""
```

## Features

---

- 이메일과 비밀번호 입력을 통해서 회원 가입을 할 수 있습니다.
/signup
body
```python
{
    "name": "name",
    "email": "kinggod2@gmail.com",
    "password": "test1234",
    "district": "강남구"
}

response 
{
    "id": 4,
    "created_at": "2022-11-10T15:42:32.878642Z",
    "updated_at": "2022-11-10T15:42:32.878642Z",
    "name": "name",
    "email": "kinggod2@gmail.com",
    "password": "$2b$12$1lQMK0.XAryaKOW1SjMNVOnAyROln6PY2tlFEHcwjQu1gmLtsBy1m",
    "district": "강남구"
}
```
- 회원 가입이후, 로그인을 할 수 있습니다.
/login
body
```python
{
    "email": "test@test.com",
    "password": "test1234"
}
response {access:"token"}
```

/get/?district_name=용산구

하수관로 수위는 현재 수위, 강수량은 24시간 누적 강수량의 강우량계별 평균입니다.

다시말해, 강우량계 숫자 * 144(상수) 만큼의 요청을 보내 전부 합한뒤 강우량계 숫자로 다시 나눠서 산출합니다.

```python
{
    "district": "용산구",
    "district_code": "03",
    "drain_pipe_water_level": 0.29,
    "measure_ymd": "2022-11-10 23:00:00.0",
    "total_rainfalls_in_day": 0,
    "summary_ymd": "2022.11.11 - 00"
}
```

getbyuser/

헤더에 담긴 토큰에 따른 유저 정보에 따라 결과값을 반환합니다.
```python
{
    "district": "성동구",
    "district_code": "04",
    "drain_pipe_water_level": 0.04,
    "measure_ymd": "2022-11-10 23:00:00.0",
    "total_rainfalls_in_day": 0,
    "summary_ymd": "2022.11.11 - 01"
}
```


### 차후 고도화 작업을 한다면

Primary
- Mock 객체에 Mock 라이브러리 사용 설정.

Secondary
- 테스트 코드 커버리지를 상승
