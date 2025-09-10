from utils.handle_mysql import *
from utils.handle_api_res_data import *



def res_precondition(res_rule, current_sheet):
    """
    获取接口返回的某指定数据
    :param res_rule: 数据规则
    :param current_sheet: sheet编号
    :return: 数据
    """
    return get_data(res_rule, current_sheet)


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


def precondition_data(condition_rule, environment, current_sheet):
    """
    使用规则获取依赖的前置数据
    :param condition_rule: 前置条件规则
    :param environment: 环境
    :param current_sheet: sheet编号
    :return: 数据
    """
    if condition_rule is not None:
        condition_rule_list = condition_rule.split("==")
        method = condition_rule_list[0]
        rule = condition_rule_list[1]
        if method == "res":
            return res_precondition(rule, current_sheet)
        elif method == "sql":
            return sql_precondition(environment, rule)
        else:
            print("仅支持从返回结果或数据库获取请求参数")




if __name__ == '__main__':
    pass
