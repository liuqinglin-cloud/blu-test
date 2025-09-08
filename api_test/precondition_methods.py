from utils.handle_mysql import *
from utils.handle_api_data import *

"""
请求参数数据依赖规则，写法如下：
    依赖某个接口的返回数据：
        res==1>data[0].id
    依赖数据库，从数据库获取：
        sql==db..field..table..factor_str
若多个字段依赖多个接口的返回数据，按照规则增加，增加处理次数即可
若多个字段依赖多个数据库的多个数据，按照规则增加，增加处理次数即可
但！若请求数据是列表类型，或者需要提前插入数据，且涉及多个表，则不实用，这种数据不好使用统一的方法处理，可使用sql方法，做好数据，并相对固定即可
"""


def res_precondition(res_rule):
    return get_data(res_rule)


def sql_precondition(environment, rule):
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
    condition_rule_list = condition_rule.split("==")
    method = condition_rule_list[0]
    rule = condition_rule_list[1]
    if method == "res":
        return res_precondition(rule)
    elif method == "sql":
        return sql_precondition(environment, rule)
    else:
        print("仅支持从返回结果或数据库获取请求参数")


if __name__ == '__main__':
    data = precondition_data("sql==blu-user-center..id..user..email='us1@qq.com'", "test_hk")
    print(data)
