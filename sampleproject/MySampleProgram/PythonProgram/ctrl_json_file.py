""" JSONファイル読み書き """
import json
from . import my_decorators


@my_decorators.my_decorator_func_s_r_e
def read_json_file_data(filename: str) -> dict:
    """ JSONファイル読み込み """
    with open(filename, "r", encoding="utf-8") as data:
        read_json_data = json.load(data)
    return read_json_data
