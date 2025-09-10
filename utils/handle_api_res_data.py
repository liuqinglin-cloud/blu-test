import json
from jsonpath_rw import parse
from utils.handle_excel import case_data



def split_data(data):
    """
    分离规则
    :param data: 获取指定返回结果中指定值的规则
    :return: 返回分离后的数据：行号（case_id）、获取返回结果指定值的规则
    """
    case_id = data.split(">")[0]
    rule_data = data.split(">")[1]
    return case_id, rule_data


def response_data(data, index):
    """
    获取返回结果
    :param data: 获取指定返回结果中指定值的规则
    :param index: sheet编号
    :return: 返回结果
    """
    case_id = split_data(data)[0]
    row_num = case_data.get_row_number(int(case_id))
    data = case_data.get_cell_value(row_num, 16, index)
    return data


def get_res_data_by_rule(res_data, rule_data):
    """
    获取返回结果中的指定值
    :param res_data: 返回结果
    :param rule_data: 获取返回结果指定值的规则
    :return: 指定值
    """
    res_data = json.loads(res_data)
    json_exe = parse(rule_data)
    model = json_exe.find(res_data)
    return [math.value for math in model][0]


def get_data(data, index):
    """
    获取指定返回结果中的指定值
    :param data: 获取指定返回结果中指定值的规则
    :param index: sheet编号
    :return: 指定值
    """
    res_data = response_data(data, index)
    rule_data = split_data(data)[1]
    return get_res_data_by_rule(res_data, rule_data)


if __name__ == '__main__':
    pass