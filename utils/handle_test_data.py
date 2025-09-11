import random
from handle_mysql import *


def generate_random_number(digits):
    """
    生成指定位数的随机数
    :param digits: 位数
    :return: 随机数
    """
    min_value = 10 ** (digits - 1)
    max_value = (10 ** digits) - 1
    return random.randint(min_value, max_value)


def generate_list_by_sql(environment ,database, table, range_str, field, length):
    """
    查询数据库数据，生成列表
    :param environment: 环境，如test_hk
    :param database: 数据库
    :param table: 表
    :param range_str: 查询条件
    :param field: 查询字段
    :param length: 列表长度
    :return: 列表
    """
    con = HandleMysql(environment, database)
    result = con.select_more(table,range_str, field)
    data_list = []
    for i in range(length):
        data_list.append(result[i][field])
    return data_list


if __name__ == '__main__':
    pass