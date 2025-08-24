from utils.handle_ini import translation_ini
from common_ios.basic_operation import *


def assert_translation_by_find_ele(section, key, num=5):
    """
    通过翻译语言定位控件，能定位到表示翻译正确
    :param section: 页面名称
    :param key: 语种名称
    :param num: 没定位到时，最大上传次数，默认5
    """
    translation = translation_ini.get_value(section,key)
    translation_list = translation.split("=")
    ele_exists = False
    for single_translation in translation_list:
        for i in range(num):
            if poco(text=single_translation).exists():
                ele_exists = True
                break
            else:
                log(f"没找到《{section}》页面《{single_translation}》元素，向上滑一下，再试试")
                swipe_bottom_top()
                sleep()
        assert_equal(ele_exists, True, f"{key}--《{section}》页面《{single_translation}》元素")


def assert_ele_is_exist(section, key, is_exist=True):
    """
    断言元素是否存在
    :param section: 页面名称
    :param key: 元素名称
    :param is_exist: 是否存在，默认断言存在
    :return:
    """
    ele = element(section,key)
    if type(ele) is not list:
        assert_equal(ele.exists(), is_exist, f"{section}页面{key}元素存在性为{is_exist}")
    else:
        log(f"{section}页面{key}元素是坐标定位")