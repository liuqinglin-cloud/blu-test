from common_ios.assert_methods import *
from common_ios.app_operation import *
from common_ios.basic_operation import click_ele_for_translation
import unittest


class TestEnglish(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log("------测试类前置处理------")
        cls.lang = "简体中文"
        ST.SAVE_IMAGE = False
        switch_lang(cls.lang)

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
        我的
        """
        log("测试------《我的》")
        click_ele_for_translation("Me")
        assert_translation_by_find_ele("我的",self.lang)

