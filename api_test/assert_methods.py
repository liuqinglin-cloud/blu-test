from utils.handle_mysql import *
from utils.handle_api_data import *
from utils.handle_redis import *


def basic_assert(expectation, result, is_equal):
    """
    断言
    :param expectation: 期望值
    :param result: 实际值
    :param is_equal: 断言相等、包含、不等
    :return: 断言结果
    """
    if is_equal == "相等":
        if result == expectation:
            return True
        else:
            return False
    elif is_equal == "包含":
        if result in expectation:
            return True
        else:
            return False
    else:
        if result == expectation:
            return False
        else:
            return True


def assert_res_data(res_rule, except_result, is_equal):
    """
    断言返回数据
    :param res_rule: 返回数据获取规则
    :param except_result: 期望值
    :param is_equal: 断言相等、包含、不等
    :return: 断言结果
    """
    res_data = get_data(res_rule)
    return basic_assert(except_result, res_data, is_equal)


def assert_sql_data(environment, rule, except_result, is_equal):
    """
    断言数据库查询数据
    :param environment: 环境
    :param rule: 规则
    :param except_result: 期望值
    :param is_equal: 断言相等、包含、不等
    :return: 断言结果
    """
    rule_sql = rule.split("=")
    db = rule_sql[0]
    field = rule_sql[1]
    table = rule_sql[2]
    factor_str = rule_sql[3]
    con = HandleMysql(environment, db)
    sql_data = con.select_one(table, factor_str, field)
    return basic_assert(except_result, sql_data, is_equal)


def assert_api(except_rule, except_result, environment):
    """
    接口断言，接口测试直接用此方法
    :param except_rule: 断言规则
    :param except_result: 期望结果
    :param environment: 环境
    :return: 断言结果
    """
    except_rule_list = except_rule.split("==")
    method = except_rule_list[0]
    rule = except_rule_list[1]
    is_equal = except_rule_list[2]
    if method == "res":
        return assert_res_data(rule, except_result, is_equal)
    elif method == "sql":
        return assert_sql_data(environment, rule, except_result, is_equal)
    else:
        print("当前只支持断言'返回结果数据'或'数据库查询数据'")
