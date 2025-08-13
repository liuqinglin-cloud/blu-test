# -*- encoding=utf8 -*-
__author__ = "admin"


import os.path
import sys
project_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_path)
from common_android.assert_methods import *
from common_android.app_operation import switch_lang, main_page
from common_android.basic_operations import click_ele_for_translation
import unittest




class TestPortuguese(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ST.SAVE_IMAGE = False
        switch_lang("葡萄牙语")
        ST.SAVE_IMAGE = True

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        ST.SAVE_IMAGE = False
        main_page()
        ST.SAVE_IMAGE = True

    def tearDown(self):
        ST.SAVE_IMAGE = False
        main_page()
        ST.SAVE_IMAGE = True

    def test_me(self):
        """
        “我的”页面翻译测试
        """
        click_ele_for_translation("Perfil")
        log("测试葡萄牙语翻译")
        assert_translation_by_find_ele("我的","葡萄牙语")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    tests = [TestPortuguese('test_me')]
    suite.addTests(tests)
    runner=unittest.TextTestRunner()
    runner.run(suite)