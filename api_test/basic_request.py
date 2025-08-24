import requests
import json


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

