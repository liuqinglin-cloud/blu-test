from common_android.assert_methods import *
from common_android.app_operation import switch_lang, main_page
from common_android.basic_operation import click_ele_for_translation
import unittest




class TestKorean(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log("------测试类前置处理------")
        ST.SAVE_IMAGE = False
        switch_lang("韩语")


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
        click_ele_for_translation("내 계정")
        assert_translation_by_find_ele("我的","韩语")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    tests = [TestKorean('test_me')]
    suite.addTests(tests)
    runner=unittest.TextTestRunner()
    runner.run(suite)