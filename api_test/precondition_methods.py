from utils.handle_mysql import *
from utils.handle_api_data import *

"""
请求参数数据依赖规则，写法如下：
    依赖某个接口的返回数据：
        数据获取方式==规则（第X个接口>数据获取规则）
        res==1>data[0].id
    依赖数据库，从数据库获取：
        数据获取方式==规则（数据库..字段..表..条件）
        sql==db..field..table..factor_str
若多个字段依赖多个接口的返回数据，按照规则增加，增加处理次数即可
若多个字段依赖多个数据库的多个数据，按照规则增加，增加处理次数即可
但！若请求数据是列表类型，或者需要提前插入数据，且涉及多个表，则不实用，这种数据不好使用统一的方法处理，可使用sql方法，做好数据，并相对固定即可
"""


def res_precondition(res_rule):
    """
    获取接口返回的某指定数据
    :param res_rule: 数据规则
    :return: 数据
    """
    return get_data(res_rule)


def sql_precondition(environment, rule):
    """
    获取指定的数据库数据
    :param environment: 环境
    :param rule: 数据库查询规则
    :return: 数据
    """
    sql_rule = rule.split("..")
    db = sql_rule[0]
    field = sql_rule[1]
    table = sql_rule[2]
    factor_str = sql_rule[3]
    con = HandleMysql(environment, db)
    select_data = con.select_one(table, factor_str, field)
    sql_data = select_data[field]
    return sql_data


def precondition_data(condition_rule, environment):
    """
    使用规则获取依赖的前置数据
    :param condition_rule: 前置条件规则
    :param environment: 环境
    :return: 数据
    """
    condition_rule_list = condition_rule.split("==")
    method = condition_rule_list[0]
    rule = condition_rule_list[1]
    if method == "res":
        return res_precondition(rule)
    elif method == "sql":
        return sql_precondition(environment, rule)
    else:
        print("仅支持从返回结果或数据库获取请求参数")

def get_token():
    """
    测试前获取token写入文件备用，或者使用的时候请求
    """
    pass


if __name__ == '__main__':
    pass
