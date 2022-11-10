import os
import yaml

yaml_settings = dict()
path = os.path.abspath(os.path.dirname(__file__))
filename = "config.yml"

with open(os.path.join(path, filename)) as f:
    yaml_settings.update(yaml.load(f, Loader=yaml.FullLoader))


class Config:
    databases: dict = yaml_settings["databases"]
    secrets: dict = yaml_settings["secrets"]
    token: dict = yaml_settings["token"]
    open_api_key: dict = yaml_settings["seoul_open_api_key"]
    DAY_DIVIDE_BY_10_MIN = 144 #상수, 1row 당 10분으로 계산


config = Config()
