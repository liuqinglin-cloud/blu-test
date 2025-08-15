from common_ios.assert_methods import *
from common_ios.app_operation import *
from common_ios.basic_operation import click_ele_for_translation
import unittest


class TestEnglish(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.lang = "简体中文"
        ST.SAVE_IMAGE = False
        switch_lang(cls.lang)
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
        click_ele_for_translation("Me")
        log("测试简体中文翻译")
        assert_translation_by_find_ele("我的",self.lang)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    tests = [TestEnglish('test_me')]
    suite.addTests(tests)
    runner=unittest.TextTestRunner()
    runner.run(suite)