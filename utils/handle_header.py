from utils.handle_json import *
from utils.handle_excel import case_data



def add_value_to_header(rule, current_sheet):
    """
    通过规则获取值，并写入header文件
    :param rule: 获取value并写入header的规则
    :param current_sheet: sheet编号
    """
    key = rule.split("=")[-1]
    rule_list = rule.split("=").pop()
    value_rule = "".join(rule_list)
    case_id = value_rule.split(">")[0]
    rule_data = value_rule.split(">")[1]
    response = case_data.get_response_data(case_id, current_sheet)
    value = get_data_by_rule(response, rule_data)
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