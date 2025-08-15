from utils.handle_ini import translation_ini
from common_android.basic_operation import *


def assert_translation_by_find_ele(section, key):
    """
    通过翻译语言定位控件，能定位到表示翻译正确
    :param section: 页面名称
    :param key: 语种名称
    :return:
    """
    translation = translation_ini.get_value(section,key)
    translation_list = translation.split("=")
    for single_translation in translation_list:
        assert_text = f"{key}--《{section}》页面《{single_translation}》元素"
        try:
            try:
                try:
                    assert_equal(poco(text=single_translation).exists(), True, assert_text)
                except:
                    log("没找到元素，向上滑一下，再试试")
                    swipe_bottom_top()
                    assert_equal(poco(text=single_translation).exists(), True, assert_text)
            except:
                log("没找到元素，再向上滑一下，再试试")
                swipe_bottom_top()
                assert_equal(poco(text=single_translation).exists(), True, assert_text)
        except:
            log("没找到元素，再再向上滑一下，再试试")
            swipe_bottom_top()
            assert_equal(poco(text=single_translation).exists(), True, assert_text)


def assert_ele_is_exist(section, key, is_exist=True):
    """
    断言元素是否存在
    :param section: 页面名称
    :param key: 元素名称
    :param is_exist: 是否存在，默认断言存在
    :return:
    """
    ele = element(section,key)
    assert_equal(ele.exists(), is_exist, f"{section}页面{key}元素存在性为{is_exist}")



