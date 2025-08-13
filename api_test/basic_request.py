import requests
import json


def send_post(url, data, cookie=None, header=None):
    response = requests.post(url=url, data=data, cookies=cookie, headers=header)
    res = response.text
    return res


def send_get(url, data, cookie=None, header=None):
    response = requests.get(url=url, params=data, cookies=cookie, headers=header)
    res = response.text
    return res


def request(method, url, data, cookie=None, header=None):
    if method == "get":
        res = send_get(url, data, cookie, header)
    else:
        res = send_post(url, data, cookie, header)
    try:
        res = json.loads(res)
    except:
        print("这个结果是一个text")
    return res

