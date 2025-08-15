from common_android.assert_methods import *
from common_android.app_operation import switch_lang, main_page
from common_android.basic_operation import click_ele_for_translation
import unittest




class TestTraditionalChinese(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ST.SAVE_IMAGE = False
        switch_lang("繁体中文")
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
        click_ele_for_translation("我的")
        log("测试繁体中文翻译")
        assert_translation_by_find_ele("我的","繁体中文")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    tests = [TestTraditionalChinese('test_me')]
    suite.addTests(tests)
    runner=unittest.TextTestRunner()
    runner.run(suite)
