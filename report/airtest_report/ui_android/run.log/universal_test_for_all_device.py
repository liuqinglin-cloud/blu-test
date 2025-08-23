import unittest

from common_android.assert_methods import *
from common_android.app_operation import *
from common_android.basic_operation import *


class TestUniversal(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ST.SAVE_IMAGE = False
        log("------测试类前置处理------")
        login_by_mail("us")
        switch_lang()
        main_page()

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

    def test_me(self):
        """
        我的
        """
        log("测试------《我的》")
        click_ele("我的", "我的")
        assert_ele_is_exist("我的", "我的账户")
        swipe_bottom_top()
        assert_ele_is_exist("我的", "订阅品牌")

    def test_push(self):
        """
        push
        """
        log("测试------《push》")
        click_ele("我的", "我的")
        click_ele("我的", "push入口")
        assert_ele_is_exist("push消息列表", "我的消息")
        swipe_bottom_top()
        click_ele("push消息列表", "设置")
        assert_ele_is_exist("push消息设置", "设备通知")

    def test_my_account(self):
        """
        我的账户
        """
        log("测试------《我的账户》")
        click_ele("我的", "我的")
        click_ele("我的", "我的账户")
        assert_ele_is_exist("我的账户", "安全中心")
        key_back()
        click_ele("我的", "头像")
        assert_ele_is_exist("我的账户", "安全中心")
        key_back()
        click_ele("我的", "昵称")
        assert_ele_is_exist("我的账户", "安全中心")
        click_ele("我的账户", "昵称")
        click_ele("通用", "确定")
        assert_ele_is_exist("我的账户", "昵称")
        click_ele("我的账户", "昵称")
        del_text("修改昵称", "输入框")
        click_ele("通用", "确定")
        assert_ele_is_exist("通用", "确定")
        key_back(2)
        click_ele("我的账户", "安全中心")
        click_ele("安全中心", "安全邮箱")
        click_ele("通用", "确定")
        assert_ele_is_exist("通用", "确定")
        click_ele("通用", "返回按钮")
        click_ele("安全中心", "更改密码")
        click_ele("通用", "确定")
        assert_ele_is_exist("通用", "确定")
        click_ele("通用", "返回按钮")
        click_ele("安全中心", "google")
        assert_ele_is_exist("google", "绑定")
        click_ele("通用", "返回按钮")
        click_ele("安全中心", "twitter")
        assert_ele_is_exist("twitter", "绑定")
        click_ele("通用", "返回按钮")
        click_ele("安全中心", "注销账户")
        click_ele("通用", "下一步")
        assert_ele_is_exist("通用", "下一步")
        key_back(3)

    def test_address(self):
        """
        地址管理
        """
        log("测试------《地址管理》")
        click_ele("我的", "我的")
        click_ele("我的", "地址管理")
        assert_ele_is_exist("地址管理", "新增地址")
        click_ele("地址管理", "新增地址")
        assert_ele_is_exist("新增地址", "名字")
        swipe_universal(0.5, 0.9, 0.5, 0.2,num=2)
        click_ele("通用", "确定")
        assert_ele_is_exist("通用", "确定")
        swipe_universal(0.5, 0.3, 0.5, 0.8)
        click_ele("新增地址", "国家地区")
        assert_ele_is_exist("国家地区", "搜索框")
        click_ele("国家地区", "搜索框")
        assert_ele_is_exist("国家地区", "搜索框")
        input_text("国家地区", "搜索框", "美国")
        select_data("US")
        click_ele("新增地址", "省州")
        assert_ele_is_exist("通用", "取消")
        click_ele("通用", "取消")
        swipe_universal(0.5, 0.9, 0.5, 0.1)
        assert_ele_is_exist("新增地址", "设为默认地址")
        click_ele("新增地址", "手机号码")
        assert_ele_is_exist("新增地址", "手机号码")
        key_back()
        click_ele("新增地址", "区号")
        assert_ele_is_exist("国家地区", "搜索框")
        click_back_button(3)

    def test_bluetti_star(self):
        pass

    def test_installer(self):
        """
        安装商
        """
        log("测试------《安装商》")
        click_ele("我的", "我的")
        click_ele("我的", "安装商")
        assert_ele_is_exist("安装商", "安装商")
        swipe_universal(0.5, 0.7, 0.5, 0.2)
        assert_ele_is_exist("安装商", "安装商")
        swipe_universal(0.5, 0.7, 0.5, 0.2)
        assert_ele_is_exist("安装商", "安装商")
        click_ele("安装商", "联系我们")
        assert_ele_is_exist("联系我们", "电话服务")
        click_back_button(2)

    def test_referral_rewards(self):
        pass

    def test_app_mark(self):
        pass

    def test_feedback(self):
        pass

    def test_sign(self):
        pass

    def test_lottery(self):
        pass

    def test_clear_cache(self):
        pass

    def test_user_agreement(self):
        pass

    def test_privacy_policy(self):
        pass

    def test_setting(self):
        pass

    def test_subscribe(self):
        pass

