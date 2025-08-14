# -*- encoding=utf8 -*-
__author__ = "admin"


import unittest
import os.path
import sys
project_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_path)
from common_android.assert_methods import assert_ele_is_exist
from common_android.app_operation import *

class TestMe(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        login_by_mail("china")
        switch_lang("简体中文")


    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_my_account(self):
        """
        测试“我的账户”各处输入框为空时，点确定，是否会出现异常
        :return:
        """
        click_ele("我的","我的")
        click_ele("我的","我的账户")
        click_ele("我的账户", "昵称")
        click_ele("通用", "确定")
        click_ele("我的账户", "安全中心")
        click_ele("安全中心", "安全邮箱")
        click_ele("通用", "确定")
        click_ele("通用", "返回按钮")
        click_ele("安全中心", "更改密码")
        click_ele("通用", "确定")
        click_ele("通用", "返回按钮")
        click_ele("安全中心", "google")
        click_ele("通用", "返回按钮")
        click_ele("安全中心", "twitter")
        click_ele("通用", "返回按钮")
        click_ele("安全中心", "注销账户")
        click_ele("通用", "下一步")
        key_back(3)

     




