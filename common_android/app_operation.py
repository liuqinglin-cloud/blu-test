from common_android.basic_operation import *
from utils.handle_ini import translation_ini, test_user_ini


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


def switch_lang(expectation="简体中文"):
    """
    切换至任意语言
    :param expectation: 期望语言的中文文案，默认简体中文
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


def main_page():
    """
    返回主页/一级页面，测试翻译要用，兼容多语言
    返回启动页，仅支持中文
    """
    upgrade()
    subscribe()
    #还需要增加点击同意协议的操作
    for i in range(10):
        main_page_info = f"经过{i}次点击返回按键，找到'我的'元素，当前在一级页面"
        start_page_info = f"经过{i}次点击返回按键，找到'无网模式'元素，当前在启动页"
        if poco(text="我的").exists():
            log(main_page_info)
            break
        elif poco(text="Me").exists():
            log(main_page_info)
            break
        elif poco(text="マイページ").exists():
            log(main_page_info)
            break
        elif poco(text="Mein").exists():
            log(main_page_info)
            break
        elif poco(text="Io").exists():
            log(main_page_info)
            break
        elif poco(text="Yo").exists():
            log(main_page_info)
            break
        elif poco(text="Moi").exists():
            log(main_page_info)
            break
        elif poco(text="내 계정").exists():
            log(main_page_info)
            break
        elif poco(text="Я").exists():
            log(main_page_info)
            break
        elif poco(text="Perfil").exists():
            log(main_page_info)
            break
        elif poco(text="无网模式").exists():
            log(start_page_info)
            break
        else:
            i += 1
            keyevent("BACK")
            sleep()
            log(f"第{i}次点击返回按键，尝试返回启动页或一级页面")
    swipe_top_bottom()


def current_environment():
    """
    App当前测试环境
    :return: 当前测试环境
    """
    logout()
    times_click_ele("启动", "logo")
    if element("开发者模式", "测试环境api").exists():
        log("当前是测试环境")
        return "测试环境"
    elif element("开发者模式", "开发环境api").exists():
        log("当前是开发环境")
        return "开发环境"
    else:
        log("当前是生产环境")
        return "生产环境"


def switch_environment(expectation):
    """
    切换App测试环境
    :param expectation: 期望的测试环境
    """
    current = current_environment()
    if expectation == current:
        log(f"当前是环境是{expectation}，不用切换")
        main_page()
    else:
        click_ele("开发者模式", expectation)
        click_ele("通用", "确定")
        log(f"环境已切换为{expectation}")
    try:
        start_app("net.poweroak.bluetticloud.debug")
        log("重启App成功")
    except:
        pass


def is_login():
    """
    判断是否是登录状态
    :return:
    """
    main_page()
    ele = element("我的", "我的")
    if ele.exists():
        log("已经是登录状态")
        return True
    else:
        log("未登录")
        return False


def login_by_mail(account_key):
    """
    邮箱登录
    :param account_key: 账号ini文件的key
    :return:
    """
    if not is_login():
        click_ele("启动", "登录")
        mail = None
        password = None
        try:
            user = test_user_ini.get_value("mail", account_key)
            mail = user.split("-")[0]
            password = user.split("-")[1]
        except:
            log(f"获取账号密码失败，请检查mail登录账号{account_key}")
        input_text("邮箱登录", "邮箱", mail)
        input_text("邮箱登录", "密码", password)
        click_ele("邮箱登录", "登录")
        click_ele("通用", "同意")
        click_ele("邮箱登录", "登录")
        sleep()
        main_page()
        ele = element("我的", "我的")
        if ele.exists():
            log("登录成功")
        else:
            log("登录失败")


def logout():
    """
    退出登录
    :return:
    """
    if is_login():
        click_ele("我的", "我的")
        click_ele("我的", "我的账户")
        click_ele("我的账户", "退出登录")
        click_ele("通用", "确定")
        ele = element("启动", "登录")
        if ele.exists():
            log("退出登录成功")
        else:
            log("退出登录失败")


def get_version():
    """
    获取App版本
    :return: 版本号
    """
    main_page()
    try:
        try:
            click_ele("我的", "我的")
            version = get_ele_text("我的", "版本")
            return version
        except:
            version = get_ele_text("启动", "版本号")
            return version
    except:
        log("当前疑似不在首页/一级页面/启动页")


def upgrade(is_upgrade=False):
    """
    升级,此操作应在订阅获取弹窗之前
    :param is_upgrade: 是否升级，默认否
    :return:
    """
    if is_upgrade is False:
        try:
            click_ele("升级弹窗", "下次再说")
        except:
            log("没有升级弹窗")
    else:
        try:
            click_ele("升级弹窗", "立即更新")
        except:
            log("没有升级弹窗")


def user_agreement(is_agree=True):
    """
    用户协议弹窗操作
    :return:
    """
    if is_agree is True:
        try:
            click_ele("通用", "同意")
        except:
            log("没有用户协议弹窗")
    else:
        try:
            click_ele("通用", "取消")
        except:
            log("没有用户协议弹窗")


def subscribe(is_subscribe=False):
    """
    订阅,此操作应在升级弹窗之后
    :param is_subscribe: 是否订阅，默认否
    :return:
    """
    if is_subscribe is False:
        try:
            click_ele("订阅获取", "30天后再提示")
        except:
            log("没有订阅弹窗")
    else:
        try:
            click_ele("订阅获取", "确认订阅")
        except:
            log("没有订阅弹窗")


def get_user_nickname():
    """
    获取用户昵称
    :return: 用户昵称
    """
    if is_login() is True:
        nickname = get_ele_text("我的", "昵称")
        return nickname


if __name__ == "__main__":
    #start_app("net.poweroak.bluetticloud.debug")
    #login_by_mail("china")
    #logout()
    #switch_lang("英语")
    #switch_environment("测试环境")
    pass
