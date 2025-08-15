# -*- encoding=utf8 -*-
__author__ = "admin"


import os.path
import sys

from PIL.ImageOps import equalize
from numpy.ma.testutils import assert_equal

project_path = os.path.dirname(os.path.dirname(__file__))
common_android_path = os.path.join(project_path,"common_android")
sys.path.append(project_path)
sys.path.append(common_android_path)
from common_android.assert_methods import *
from common_android.app_operation import *
from common_android.basic_operation import click_ele
import unittest






class TestSimplifiedChinese(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.lang = "简体中文"
        ST.SAVE_IMAGE = False
        login_by_mail("china")
        switch_lang(cls.lang)
        log("测试简体中文翻译")
        ST.SAVE_IMAGE = True

    @classmethod
    def tearDownClass(cls):
        ST.SAVE_IMAGE = False
        main_page()
        ST.SAVE_IMAGE = True

    def setUp(self):
        pass

    def tearDown(self):
        ST.SAVE_IMAGE = False
        main_page()
        swipe_top_bottom()
        ST.SAVE_IMAGE = True

    def test_me(self):
        """
        “我的”页面翻译测试
        """
        click_ele("我的","我的")
        assert_translation_by_find_ele("我的",self.lang)

    def test_my_account(self):
        """
        “我的账户”翻译测试
        """
        click_ele("我的", "我的")
        click_ele("我的", "我的账户")
        assert_translation_by_find_ele("我的账户", self.lang)
        click_ele("我的账户", "昵称")
        assert_translation_by_find_ele("修改昵称", self.lang)
        click_ele("通用", "确定")
        click_ele("我的账户", "安全中心")
        assert_translation_by_find_ele("安全中心", self.lang)
        click_ele("安全中心", "安全邮箱")
        assert_translation_by_find_ele("安全邮箱", self.lang)
        key_back()
        click_ele("安全中心", "更改密码")
        assert_translation_by_find_ele("更改密码", self.lang)
        key_back()
        click_ele("安全中心", "google")
        assert_translation_by_find_ele("google账号绑定", self.lang)
        key_back()
        click_ele("安全中心", "twitter")
        assert_translation_by_find_ele("twitter账号绑定", self.lang)
        key_back()
        click_ele("安全中心", "注销账户")
        assert_translation_by_find_ele("注销账户", self.lang)
        key_back(3)

    def test_address(self):
        """
        “地址管理”翻译测试
        """
        click_ele("我的", "我的")
        click_ele("我的", "地址管理")
        assert_translation_by_find_ele("地址管理", self.lang)
        click_ele("地址管理", "新增地址")
        assert_translation_by_find_ele("新增地址", self.lang)
        swipe_top_bottom()
        swipe_top_bottom()
        swipe_bottom_top()
        click_ele("新增地址", "国家地区")
        assert_translation_by_find_ele("国家地区", self.lang)
        input_text("国家地区","搜索框","美国")
        click_ele_for_translation("US")
        click_ele("新增地址", "省州")
        assert_translation_by_find_ele("省州", self.lang)
        key_back(3)



if __name__ == "__main__":
    suite = unittest.TestSuite()
    tests = [TestSimplifiedChinese("test_my_account")]
    suite.addTests(tests)
    runner=unittest.TextTestRunner()
    runner.run(suite)

