# -*- encoding=utf8 -*-
__author__ = "admin"

import os.path
import sys

project_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_path)
from common_ios.basic_operation import *
from utils.handle_ini import translation_ini,test_user_ini

def main_page():
    pass

def current_lang():
    """
    判断当前语言
    :return: 当前语言，格式为中文字符串
    """
    main_page()
    try:
        poco0 = poco(text="服务")
        poco1 = poco(text="Me")
        poco2 = poco(text="マイページ")
        poco3 = poco(text="Mein")
        poco4 = poco(text="Io")
        poco5 = poco(text="Yo")
        poco6 = poco(text="Moi")
        poco7 = poco(text="내 계정")
        poco8 = poco(text="Я")
        poco9 = poco(text="Perfil")
        if poco0.exists():
            return "简体中文"
        elif poco1.exists():
            return "英语"
        elif poco2.exists():
            return "日语"
        elif poco3.exists():
            return "德语"
        elif poco4.exists():
            return "意大利语"
        elif poco5.exists():
            return "西班牙语"
        elif poco6.exists():
            return "法语"
        elif poco7.exists():
            return "韩语"
        elif poco8.exists():
            return "乌克兰语"
        elif poco9.exists():
            return "葡萄牙语"
        else:
            return "繁体中文"
    except:
        log("获取当前语言失败，请检查是否为登录状态")

def switch_lang(expectation):
    """
    切换至任意语言
    :param expectation: 期望语言的中文文案，如英语
    """
    lang = current_lang()
    log(f"当前语言是{lang}")
    if lang == expectation:
        log(f"期望语言是{expectation}，那就不用切换语言了")
    else:
        data = translation_ini.get_value(section="当前语言", key=lang)
        data_list = data.split("-")
        me = data_list[0]
        settings = data_list[1]
        languages = data_list[2]
        confirm_button = data_list[3]
        expectation_lang = translation_ini.get_value(section="期望语言", key=expectation)
        poco(text=me).click()
        sleep()
        try:
            poco(text=settings).click()
        except:
            swipe_bottom_top()
            poco(text=settings).click()
        poco(text=languages).click()
        try:
            poco(text=expectation_lang).click()
        except:
            swipe_bottom_top()
            poco(text=expectation_lang).click()
        poco(text=confirm_button).click()
        log(f"已切换语言为{expectation}")
        sleep(3)
        main_page()

if __name__ == "__main__":
    pass
