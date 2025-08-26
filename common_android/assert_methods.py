from utils.handle_ini import translation_ini
from common_android.basic_operation import *


def assert_translation_by_find_ele(section, key="简体中文", num=6, expectation=None):
    """
    通过翻译语言定位控件，能定位到表示翻译正确
    :param section: 页面名称
    :param key: 语种名称，默认简体中文
    :param num: 如果没找到，上滑后再尝试，最大上滑次数，默认6
    :param expectation: 期望值，无法直接通过定位断言，可以获取文本传入
    """
    translation = translation_ini.get_value(section,key)
    translation_list = translation.split("==")
    ele_exists = False
    if expectation is None:
        for single_translation in translation_list:
            for i in range(num):
                if poco(text=single_translation).exists():
                    ele_exists = True
                    break
                else:
                    log(f"没找到《{section}》页面《{single_translation}》元素，向上滑一下，再试试")
                    swipe_universal(0.5,0.6,0.5,0.3)
                    sleep()
            assert_equal(ele_exists, True, f"{key}--《{section}》页面《{single_translation}》元素")
    else:
        for single_translation in translation_list:
            if single_translation in expectation:
                ele_exists = True
            assert_equal(ele_exists, True, f"{key}相关元素--《{section}》页面《{single_translation}》文案")



def assert_ele_is_exist(section, key, is_exist=True):
    """
    断言元素是否存在
    :param section: 页面名称
    :param key: 元素名称
    :param is_exist: 是否存在，默认断言存在
    """
    ele = element(section,key)
    if type(ele) is not list:
        assert_equal(ele.exists(), is_exist, f"《{section}》页面《{key}》元素存在性为{is_exist}")
    else:
        log(f"《{section}》页面《{key}》元素是坐标定位")


def assert_ele_text(section,key,txt,is_equal=True):
    """
    断言元素文本
    :param section: 页面名称
    :param key: 元素名称
    :param txt: 期望文本
    :param is_equal: 文本是否一致，默认一致
    """
    ele_text = get_ele_text(section,key)
    if is_equal is True:
        assert_equal(ele_text,txt,f"《{section}》页面《{key}》元素文本是{txt}")
    else:
        assert_not_equal(ele_text,txt,f"《{section}》页面《{key}》元素文本不是{txt}")