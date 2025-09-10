from utils.handle_api_res_data import get_data
from utils.handle_json import *


def add_value_to_header(rule, current_sheet):
    """
    通过规则获取值，并写入header文件
    :param rule: 获取value并写入header的规则
    :param current_sheet: sheet编号
    """
    key = rule.split("=")[-1]
    rule_list = rule.split("=").pop()
    value_rule = "".join(rule_list)
    value = get_data(value_rule, current_sheet)
    header_json.add_value(key, value)

def get_header():
    """
    读取header文件
    :return: header
    """
    return header_json.read_json_file()

def handle_header(rule, current_sheet):
    """
    接口测试处理header
    :param rule: header处理规则
    :param current_sheet: sheet编号
    :return: header
    """
    if rule == "yes":
        return get_header()
    elif rule == "no":
        return None
    else:
        add_value_to_header(rule, current_sheet)
        return get_header()



if __name__ == '__main__':
    pass