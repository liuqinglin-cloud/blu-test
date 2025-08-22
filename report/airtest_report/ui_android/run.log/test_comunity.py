import unittest

from common_android.assert_methods import *
from common_android.app_operation import *
from common_android.basic_operation import *


class TestMe(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ST.SAVE_IMAGE = False
        log("------测试类前置处理------")
        login_by_mail("us")
        switch_lang("简体中文")

    @classmethod
    def tearDownClass(cls):
        log("------测试类后置处理------")
        pass

    def setUp(self):
        log("------测试方法前置处理------")
        pass
        ST.SAVE_IMAGE = True

    def tearDown(self):
        ST.SAVE_IMAGE = False
        log("------测试方法后置处理------")
        main_page()
        swipe_top_bottom()

