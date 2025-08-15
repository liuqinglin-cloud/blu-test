from utils.handle_ini import local_element_ios_ini
from airtest.core.api import *
from airtest.cli.parser import cli_setup
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/1C231FDF60050J?cap_method=ADBCAP&touch_method=MAXTOUCH&",])

from poco.drivers.ios import iosPoco
poco = iosPoco()



def swipe_bottom_top():
    pass

def swipe_top_bottom():
    pass

def element(section,key):
    """
        获取ini元素，创建UIObjectProxy
        :param section: 页面名字
        :param key: 元素名字
        :return: 定位方式是position返回position，其他返回UIObjectProxy
        """
    value = local_element_ios_ini.get_value(section, key)
    if value:
        if "=" not in value:
            ele = poco(text=value)
            log(f"获取到《{section}》页面《{key}》元素text定位信息")
            return ele
        else:
            value_list = value.split("=")
            method = value_list[0]
            log_info_success = f"获取到《{section}》页面《{key}》元素{method}定位信息"
            log_info_fail = f"《{section}》页面《{key}》元素{method}定位方式，属性值写法不符合要求"
            if method == "name":
                try:
                    ele_attribute_name = value_list[1]
                    log(log_info_success)
                    ele = poco(name=ele_attribute_name)
                    return ele
                except:
                    log(log_info_fail)
            elif method == "position":
                try:
                    x = int(value_list[1])
                    y = int(value_list[2])
                    log(log_info_success)
                    position = [x, y]
                    return position
                except:
                    log(log_info_fail)
            elif method == "name&text":
                try:
                    ele_attribute_name = value_list[1]
                    ele_attribute_text = value_list[2]
                    log(log_info_success)
                    ele = poco(name=ele_attribute_name, text=ele_attribute_text)
                    return ele
                except:
                    log(log_info_fail)
            elif method == "RegExp_name_text":
                try:
                    regexp_name = value_list[1]
                    regexp_text = value_list[2]
                    log(log_info_success)
                    ele = poco(nameMatches=regexp_name, textMatches=regexp_text)
                    return ele
                except:
                    log(log_info_fail)
            elif method == "RegExp_name_type":
                try:
                    regexp_name = value_list[1]
                    regexp_type = value_list[2]
                    log(log_info_success)
                    ele = poco(nameMatches=regexp_name, typeMatches=regexp_type)
                    return ele
                except:
                    log(log_info_fail)
            elif method == "path":
                path_list = value_list.pop(0)
                path_list_len = len(path_list)
                paths = []
                for i in range(path_list_len):
                    path_x = "path_" + str(i)
                    paths.append(path_x)
                for i in range(path_list_len):
                    locals()[paths[i]] = path_list
                log("当前无法实现通用的path定位")
            else:
                log(f"定位方式《{method}》不符合规则")
    else:
        log(f"请检查《{section}》页面《{key}》元素文件")

def ele_is_exist(section,key):
    """
        判断元素是否存在，存在则返回UIObjectProxy或position
        :param section: 页面名称
        :param key: 元素名称
        :return: 定位方式是position返回position，其他返回UIObjectProxy
        """
    ele = element(section, key)
    if ele is not None:
        if type(ele) is not list:
            if ele.exists():
                log(f"定位到《{section}》页面《{key}》元素")
                return ele
            else:
                log(f"没有定位到《{section}》页面《{key}》元素")
        else:
            return ele


