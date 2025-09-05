from utils.handle_mysql import *
from utils.handle_api_data import *


def res_precondition(res_rule):
    return get_data(res_rule)

def sql_precondition():
    pass


def precondition_data(condition_rule, environment):
    condition_rule_list = condition_rule.split("==")
    method = condition_rule_list[0]
    rule = condition_rule_list[1]
    if method == "res":
        return res_precondition(rule)
    elif method == "sql":
        rule_list = rule.split(">")
        sql_method = rule_list[0]
        if sql_method == "select":
            sql_parameter_list = rule_list[1].split()
        pass
    else:
        print("前置处理失败")







"""
前置条件：res==1>data[0].id
        sql==查询>db...
"""