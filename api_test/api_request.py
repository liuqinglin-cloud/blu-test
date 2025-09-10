import demjson3
import requests
import json
from api_test.assert_methods import assert_api
from api_test.precondition_methods import precondition_data
from utils.handle_cookie import handle_cookie
from utils.handle_excel import case_data
from utils.handle_header import handle_header
from utils.handle_ini import environment_ini


def send_post(url, data, cookie=None, header=None):
    """
    post请求
    :param url: 接口
    :param data: 参数
    :param cookie: cookie，默认None
    :param header: header，默认None
    :return: 结果
    """
    response = requests.post(url=url, data=data, cookies=cookie, headers=header)
    res = response.text
    return res


def send_get(url, data, cookie=None, header=None):
    """
    get请求
    :param url: 接口
    :param data: 参数
    :param cookie: cookie，默认None
    :param header: header，默认None
    :return: 结果
    """
    response = requests.get(url=url, params=data, cookies=cookie, headers=header)
    res = response.text
    return res


def request(method, url, data, cookie=None, header=None):
    """
    统一的请求
    :param method: 方式
    :param url: 接口
    :param data: 参数
    :param cookie: cookie，默认None
    :param header: header，默认None
    :return: 结果
    """
    if method == "get":
        res = send_get(url, data, cookie, header)
    else:
        res = send_post(url, data, cookie, header)
    try:
        res = json.loads(res)
    except:
        print("这个结果是一个text")
    return res

def run_request(data,current_sheet):
    """
    执行测试请求
    :param data: 测试数据
    :param current_sheet: 测试数据所在的sheet编号
    """
    is_run = data[2]
    case_id = data[0]
    row_num = case_data.get_row_number(case_id)
    if is_run == "yes":
        precondition_rule = data[3]
        environment = data[5]
        depend_data = precondition_data(precondition_rule, environment, current_sheet)
        depend_key = data[4]
        request_data = json.loads(data[9])
        try:
            if depend_key is not None:
                request_data[depend_key] = depend_data
                request_data = demjson3.encode(request_data)
            method = data[8]
            url = data[7]
            server_name = data[6]
            host = environment_ini.get_value(server_name, environment)
            url = host + url
            except_rule = data[12]
            except_result = data[13]
            cookie_method = data[10]
            cookie = handle_cookie(cookie_method)
            header_method = data[11]
            header = handle_header(header_method, current_sheet)
            res = request(method, url, request_data, cookie, header)
            case_data.excel_write_data(current_sheet, row_num, 16, json.dumps(res, ensure_ascii=False))
            assert_result = assert_api(except_rule, except_result, environment, current_sheet)
            if assert_result is True:
                case_data.excel_write_data(current_sheet, row_num, 15, "通过")
            else:
                case_data.excel_write_data(current_sheet, row_num, 15, "失败")
                raise Exception
        except Exception as e:
            case_data.excel_write_data(current_sheet, row_num, 15, "失败")
            raise e
