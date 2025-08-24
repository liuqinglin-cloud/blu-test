import json
from jsonpath_rw import parse
from utils.handle_excel import case_data



def split_data(data):
    """
    分离前置条件precondition，分为依赖的case编号和依赖的数据规则
    :param data: 前置条件数据
    :return: 返回分离后的数据
    """
    case_id = data.split(">")[0]
    rule_data = data.split(">")[1]
    return case_id, rule_data


def dependent_data(data):
    """
    获取整体依赖数据：依赖case的结果数据
    :param data: 前置条件数据
    :return: 依赖的结果数据
    """
    case_id = split_data(data)[0]
    row_num = case_data.get_row_number(int(case_id))
    data = case_data.get_cell_value(row_num, 16)
    return data


def get_dependent_data(res_data, key):
    """
    获取具体的依赖字段数据
    :param res_data: 依赖的结果数据
    :param key: 前置条件的依赖数据规则
    :return: 依赖数据
    """
    res_data = json.loads(res_data)
    json_exe = parse(key)
    model = json_exe.find(res_data)
    return [math.value for math in model][0]


def get_data(data):
    """
    获取依赖数据
    :param data: precondition的数据
    :return: 依赖数据
    """
    res_data = dependent_data(data)
    rule_data = split_data(data)[1]
    return get_dependent_data(res_data, rule_data)


if __name__ == '__main__':
    pre = get_data("1>data[0].id")
    print(pre)