# -*- encoding=utf8 -*-
__author__ = "admin"


from basic_operations import *



def sys_photo_permission_setting(permission="始终全部允许"):
    """
    系统设置APP照片权限，pixel6
    :param permission: 三选一"不允许"、"始终全部允许"（默认）、"每次都询问"
    :return:
    """
    stop_app("com.android.settings")
    clear_app("com.android.settings")
    start_app("com.android.settings")
    click_ele("pixel6手机", "应用")
    ele = element("pixel6手机", "测试应用")
    if ele.exists():
        ele.click()
    else:
        click_ele("pixel6手机", "所有应用")
        for i in range(10):
            if ele.exists():
                ele.click()
                break
            else:
                swipe_bottom_top()
    click_ele("pixel6手机", "权限")
    click_ele("pixel6手机", "照片和视频")
    click_ele("pixel6手机", permission)
    home()

def switch_wifi():
    """
    原计划使用poco，页面操作，直接传入wifi名字，切换WiFi，
    但是wifi不稳定造成连接时间不确定，
    所以建议使用adb连接wifi
    """
    pass




