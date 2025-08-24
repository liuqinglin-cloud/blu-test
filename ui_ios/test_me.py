import unittest

from common_ios.assert_methods import *
from common_ios.app_operation import *


class TestMe(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log("------测试类前置处理------")
        ST.SAVE_IMAGE = False
        switch_lang("简体中文")

    @classmethod
    def tearDownClass(cls):
        log("------测试类后置处理------")
        pass

    def setUp(self):
        log("------测试方法前置处理------")
        main_page()
        ST.SAVE_IMAGE = True

    def tearDown(self):
        log("------测试方法后置处理------")
        ST.SAVE_IMAGE = False
        main_page()


    def test_me(self):
        """
        我的账户
        """
        log("测试------《我的账户》")
        click_ele("我的","我的")
        click_ele("我的", "头像")
        assert_ele_is_exist("我的账户","安全中文")