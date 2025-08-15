from common_ios.basic_operation import *
from utils.handle_ini import translation_ini,test_user_ini

def main_page():
    """
    返回主页/一级页面，测试翻译要用，兼容多语言
    返回启动页，仅支持中文
    """
    #upgrade()
    #subscribe()
    # 还需要增加点击同意协议的操作
    for i in range(10):
        main_page_info = f"经过{i}次点击返回按键，找到'我的'元素，当前在一级页面"
        start_page_info = f"经过{i}次点击返回按键，找到'无网模式'元素，当前在启动页"
        if poco("我的").exists():
            log(main_page_info)
            break
        elif poco("Me").exists():
            log(main_page_info)
            break
        elif poco("マイページ").exists():
            log(main_page_info)
            break
        elif poco("Mein").exists():
            log(main_page_info)
            break
        elif poco("Io").exists():
            log(main_page_info)
            break
        elif poco("Yo").exists():
            log(main_page_info)
            break
        elif poco("Moi").exists():
            log(main_page_info)
            break
        elif poco("내 계정").exists():
            log(main_page_info)
            break
        elif poco("Я").exists():
            log(main_page_info)
            break
        elif poco("Perfil").exists():
            log(main_page_info)
            break
        elif poco("无网模式").exists():
            log(start_page_info)
            break
        else:
            i += 1
            click_ele("通用", "返回按钮")
            sleep()
            log(f"第{i}次点击返回按钮，尝试返回启动页或一级页面")

def current_lang():
    """
    判断当前语言
    :return: 当前语言，格式为中文字符串
    """
    main_page()
    try:
        poco0 = poco("服务")
        poco1 = poco("Me")
        poco2 = poco("マイページ")
        poco3 = poco("Mein")
        poco4 = poco("Io")
        poco5 = poco("Yo")
        poco6 = poco("Moi")
        poco7 = poco("내 계정")
        poco8 = poco("Я")
        poco9 = poco("Perfil")
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
        poco(me).click()
        sleep()
        try:
            poco(settings).click()
        except:
            swipe_bottom_top()
            poco(settings).click()
        poco(languages).click()
        try:
            poco(expectation_lang).click()
        except:
            swipe_bottom_top()
            poco(expectation_lang).click()
        poco(confirm_button).click()
        log(f"已切换语言为{expectation}")
        sleep(3)
        main_page()

if __name__ == "__main__":
    switch_lang("英语")
    pass
