from common_android.assert_methods import *
from common_android.app_operation import *
from common_android.basic_operation import click_ele_for_translation
import unittest


class TestEnglish(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.lang = "英语"
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