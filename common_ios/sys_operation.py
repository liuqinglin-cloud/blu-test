from basic_operation import *



def sys_photo_permission_setting(permission="完全访问"):
    """
    系统设置BLUETTI-BETA照片访问权限
    :param permission: 权限，"完全访问"、"受限访问"、"无"三选一，默认"完全访问"
    :return:
    """
    home()
    click_ele("ios","设置")
    swipe_bottom_top(400)
    click_ele("ios", "隐私与安全性")
    click_ele("ios", "照片")
    click_ele("ios", "BLUETTI-BETA")
    click_ele("ios", permission)
    click_ele("ios", "允许完全访问")
    home()





if __name__ == "__main__":
    sys_photo_permission_setting()
    pass