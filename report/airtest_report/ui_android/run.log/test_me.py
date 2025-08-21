import unittest

from common_android.assert_methods import assert_ele_is_exist
from common_android.app_operation import *
from common_android.basic_operation import *

class TestMe(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        login_by_mail("us")
        switch_lang("简体中文")


    @classmethod
    def tearDownClass(cls):
        main_page()
        swipe_top_bottom()

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_my_account(self):
        """
        测试“我的账户”各处输入框为空时，点确定，是否会出现异常
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

    def test_address(self):
        """
        测试“地址管理”各处输入框为空等情况，点确定，是否会出现异常
        """
        click_ele("我的", "我的")
        click_ele("我的", "地址管理")
        click_ele("地址管理", "新增地址")
        swipe_bottom_top(num=2)
        click_ele("通用", "确定")
        swipe_top_bottom(num=2)
        key_del_text("新增地址", "联系邮箱")
        swipe_bottom_top(num=2)
        click_ele("通用", "确定")
        click_ele("新增地址", "设为默认地址")
        click_ele("通用", "确定")
        key_back(2)

    def test_feedback(self):
        """
        测试“地址管理”各处输入框为空等情况，点确定，是否会出现异常
        """
        click_ele("我的", "我的")
        click_ele("我的", "问题反馈")
        click_ele("问题反馈", "自助报障")
        click_ele("自助报障", "提交")
        key_del_text("自助报障", "联系人")
        key_del_text("自助报障", "邮箱")
        click_ele("自助报障", "提交")
        key_back()
        click_ele("问题反馈", "物流")
        click_ele("物流", "提交")
        key_del_text("物流", "联系人")
        key_del_text("物流", "邮箱")
        click_ele("物流", "提交")
        key_back()
        click_ele("问题反馈", "客服问题")
        click_ele("客服问题", "提交")
        key_del_text("客服问题", "联系人")
        key_del_text("客服问题", "邮箱")
        click_ele("客服问题", "提交")
        key_back()
        click_ele("问题反馈", "BLUETTI APP")
        click_ele("BLUETTI APP", "提交")
        key_del_text("BLUETTI APP", "联系人")
        key_del_text("BLUETTI APP", "邮箱")
        click_ele("BLUETTI APP", "提交")
        key_back(2)
