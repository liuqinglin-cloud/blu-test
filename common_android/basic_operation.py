from utils.handle_ini import local_element_android_ini
from airtest.core.api import *
from airtest.cli.parser import cli_setup
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/1C231FDF60050J?cap_method=ADBCAP&touch_method=MAXTOUCH&",])

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=True)

ST.FIND_TIMEOUT = 20
ST.FIND_TIMEOUT_TMP = 3
sleep(1)

"""
class BasicOperation:
    
    def __init__(self):
        if not cli_setup():
            auto_setup(__file__, 
                       logdir=True,
                       devices=["android://127.0.0.1:5037/1C231FDF60050J?cap_method=ADBCAP&touch_method=MAXTOUCH&", ])
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
"""

def element(section,key):
    """
    获取ini元素，创建UIObjectProxy
    :param section: 页面名字
    :param key: 元素名字
    :return: 定位方式是position返回position，其他返回UIObjectProxy
    """
    value = local_element_android_ini.get_value(section, key)
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
                    position = [x,y]
                    return position
                except:
                    log(log_info_fail)
            elif method == "name&text":
                try:
                    ele_attribute_name = value_list[1]
                    ele_attribute_text = value_list[2]
                    log(log_info_success)
                    ele = poco(name=ele_attribute_name,text=ele_attribute_text)
                    return ele
                except:
                    log(log_info_fail)
            elif method == "RegExp_name_text":
                try:
                    regexp_name = value_list[1]
                    regexp_text = value_list[2]
                    log(log_info_success)
                    ele = poco(nameMatches=regexp_name,textMatches=regexp_text)
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
                    path_x = "path_"+str(i)
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
    ele = element(section,key)
    if ele is not None:
        if type(ele) is not list:
            if ele.exists():
                log(f"定位到《{section}》页面《{key}》元素")
                return ele
            else:
                log(f"没有定位到《{section}》页面《{key}》元素")
        else:
            return ele

def click_ele(section,key):
    """
    单击元素
    :param section: 页面名字
    :param key: 元素名字
    :return:
    """
    ele = ele_is_exist(section,key)
    if ele:
        log_info_success = f"点击《{section}》页面《{key}》元素成功"
        log_info_fail = f"点击《{section}》页面《{key}》元素失败"
        if type(ele) is not list:
            try:
                try:
                    ele.click()
                    log(log_info_success)
                except:
                    position = ele.get_position()
                    click(position)
                    log(log_info_success)
            except:
                log(log_info_fail)
        else:
            try:
                click(ele)
                log(log_info_success)
            except:
                log(log_info_fail)

def long_click_ele(section,key,duration=2):#
    """
    长按元素
    :param section: 页面名称
    :param key: 元素名称
    :param duration: 长按时间，默认2
    :return:
    """
    ele = ele_is_exist(section, key)
    if ele:
        log_info_success = f"长按《{section}》页面《{key}》元素成功"
        log_info_fail = f"长按《{section}》页面《{key}》元素失败"
        if type(ele) is not list:
            try:
                try:
                    ele.long_click(duration=duration)
                    log(log_info_success)
                except:
                    position = ele.get_position()
                    touch(position, duration=duration)
                    log(log_info_success)
            except:
                log(log_info_fail)
        else:
            try:
                touch(ele,duration=duration)
                log(log_info_success)
            except:
                log(log_info_fail)

def double_click_ele(section,key):
    """
    双击元素
    :param section: 页面名称
    :param key: 元素名称
    :return:
    """
    ele = ele_is_exist(section, key)
    if ele:
        position = ele
        if type(ele) is not list:
            position = ele.get_position()
        try:
            try:
                double_click(position)
                log(f"双击《{section}》页面《{key}》元素成功")
            except:
                touch(position, duration=0.2, times=2)
                log(f"双击《{section}》页面《{key}》元素成功")
        except:
            log(f"双击《{section}》页面《{key}》元素失败")

def times_click_ele(section,key,times=5):
    """
    连续点击N次元素，请在多次点击后断言确保无异常
    :param section: 页面名称
    :param key: 元素名称
    :param times: 次数，默认5次
    :return:
    """
    ele = ele_is_exist(section, key)
    if ele:
        position = ele
        if type(ele) is not list:
            position = ele.get_position()
        try:
            touch(position, duration=0.2, times=times)
            log(f"连续点击{times}次《{section}》页面《{key}》元素成功")
        except:
            log(f"连续点击{times}次《{section}》页面《{key}》元素失败")

def click_ele_for_translation(ele_attribute):
    """
    翻译专用，一般测试的元素定位属性都写在ini文件，是中文格式，
    不值得每个语种维护一套，所以测试翻译时，需要传入元素对应语言属性值定位并点击，
    此处仅支持text或name定位，其他定位方式可使用通用点击
    :param ele_attribute: 元素属性
    :return:
    """
    try:
        try:
            poco(text=ele_attribute).click()
            log("text定位点击元素成功")
            sleep()
        except:
            poco(name=ele_attribute).click()
            log("name定位点击元素成功")
            sleep()
    except:
        log("点击元素失败")

def key_back(times=1):
    """
    安卓key_event返回
    :param times: 次数，默认1
    :return:
    """
    log(f"计划点击{times}次返回按键")
    for i in range(times):
        keyevent("BACK")
        i += 1
        log(f"第{i}次点击返回按键成功")
        sleep()

def click_back_button(times=1):
    """
    点击返回按钮，慎用
    :param times: 次数，默认1
    :return:
    """
    log(f"计划点击{times}次返回按钮")
    for i in range(times):
        i += 1
        try:
            click_ele("通用", "返回按钮")
            sleep()
            log(f"第{i}次点击返回按钮成功")
        except:
            log(f"第{i}次点击,没有找到返回按钮，停止点击")
            break

def swipe_bottom_top(coordinates=1900):
    """
    从下往上滑动，展示下方内容
    :coordinates:起点纵坐标，根据不同手机自定义,默认pixel6可用
    :return:
    """
    swipe((500, coordinates), (500, 500))
    log("从下往上滑动，展示下方内容")

def swipe_top_bottom(coordinates=1900):
    """
    从上往下滑动,展示上方内容
    :coordinates:终点纵坐标，根据不同手机自定义,默认pixel6可用
    :return:
    """
    swipe((500, 500), (500, coordinates))
    log("从上往下滑动,展示上方内容")

def swipe_left_right(coordinates=1186):
    """
    从左往右滑动，展示左方内容
    :coordinates:纵坐标，根据不同手机自定义,默认pixel6可用
    :return:
    """
    swipe((172, coordinates), (899, coordinates))
    log("从左往右滑动，展示左方内容")

def swipe_right_left(coordinates=1186):
    """
    从右往左滑动，展示右方内容
    :coordinates:纵坐标，根据不同手机自定义,默认pixel6可用
    :return:
    """
    swipe((899, coordinates), (172, coordinates))
    log("从右往左滑动，展示右方内容")

def get_ele_text(section,key):
    """
    获取元素文案
    :param section: 页面名称
    :param key: 元素名称
    :return: 元素文案
    """
    ele = ele_is_exist(section, key)
    if ele:
        if type(ele) is not list:
            try:
                ele_text = ele.get_text()
                log(f"获取到《{section}》页面《{key}》元素文本内容：{ele_text}")
                return ele_text
            except:
                log(f"没有获取到《{section}》页面《{key}》元素文本内容")
        else:
            log(f"《{section}》页面《{key}》元素是坐标定位")

def get_len_of_text(section,key):
    """
    获取元素文本长度
    :param section: 页面名称
    :param key: 元素名称
    :return: 元素文本长度
    """
    ele_text = get_ele_text(section,key)
    len_of_text = len(ele_text)
    return len_of_text

def del_text(section,key):
    """
    删除输入框的文本
    :param section: 页面名称
    :param key: 元素名称
    :return:
    """
    text1 = get_ele_text(section,key)
    len_text = len(text1)
    click_ele(section,key)
    log(f"《{section}》页面《{key}》元素，需要按{len_text}次删除按键删除内容")
    for i in range(len_text):
        keyevent("KEYCODE_DEL")
        i += 1
        log(f"第{i}次按删除按键")
    text2 = get_ele_text(section, key)
    if text2 not in text1:
        log(f"《{section}》页面《{key}》元素内容删除完成")
    else:
        log("删除异常，请检查")

def input_text(section,key,txt):
    """
    poco输入内容,输入前不需要清除
    :param section: 页面名字
    :param key: 元素名字
    :param txt: 输入内容
    :return:
    """
    ele = ele_is_exist(section, key)
    if ele:
        if type(ele) is not list:
            try:
                ele.set_text(txt)
                log(f"《{section}》页面《{key}》元素输入{txt}成功")
            except:
                log(f"《{section}》页面《{key}》元素输入{txt}失败")
        else:
            log(f"《{section}》页面《{key}》元素是坐标定位")

def input_text_enter(section,key,txt):
    """
    输入内容并按回车键，采用airtest输入，有时会失败，输入后应该检查
    :param section: 页面名字
    :param key: 元素名字
    :param txt: 输入内容
    :return:
    """
    del_text(section,key)
    try:
        text(txt,enter=True)
        log(f"《{section}》页面《{key}》元素输入{txt}并按回车键")
    except:
        log(f"《{section}》页面《{key}》元素'输入{txt}并按回车键'操作失败")

def input_text_search(section,key,txt):
    """
    输入内容并搜索，，采用airtest输入，有时会失败，输入后应该检查
    :param section: 页面名字
    :param key: 元素名字
    :param txt: 输入内容
    :return:
    """
    del_text(section,key)
    try:
        text(txt,search=True)
        log(f"《{section}》页面《{key}》元素输入{txt}并搜索")
    except:
        log(f"《{section}》页面《{key}》元素'输入{txt}并搜索'操作失败")

if __name__ == "__main__":
    pass