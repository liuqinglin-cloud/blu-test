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

    def test_my_account(self):
        """
        测试“我的账户”各处输入框为空时，点确定，是否会出现异常
        """
        log("测试------《我的账户》")
        click_ele("我的","我的")
        click_ele("我的","我的账户")
        click_ele("我的账户", "昵称")
        click_ele("通用", "确定")
        assert_ele_is_exist("我的账户", "昵称")
        click_ele("我的账户", "昵称")
        del_text("修改昵称","输入框")
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
        click_ele("通用", "返回按钮")
        click_ele("安全中心", "twitter")
        click_ele("通用", "返回按钮")
        click_ele("安全中心", "注销账户")
        click_ele("通用", "下一步")
        assert_ele_is_exist("通用", "下一步")
        key_back(3)

    def test_address(self):
        """
        测试“地址管理”各处输入框为空等情况，点确定，是否会出现异常
        """
        log("测试------《地址管理》")
        click_ele("我的", "我的")
        click_ele("我的", "地址管理")
        click_ele("地址管理", "新增地址")
        swipe_bottom_top(num=2)
        click_ele("通用", "确定")
        assert_ele_is_exist("通用", "确定")
        swipe_top_bottom(num=2)
        key_del_text("新增地址", "联系邮箱")
        key_back()
        swipe_bottom_top(num=2)
        click_ele("通用", "确定")
        assert_ele_is_exist("通用", "确定")
        click_ele("新增地址", "设为默认地址")
        click_ele("通用", "确定")
        assert_ele_is_exist("通用", "确定")
        key_back(2)

    def test_app_mark(self):
        """
        app评分跳转测试
        """
        log("测试------《app评分跳转测试》")
        click_ele("我的", "App评分")
        assert_ele_is_exist("pixel6手机","商店登录")
        home()
        start_app("net.poweroak.bluetticloud.debug")

    def test_feedback(self):
        """
        测试“问题反馈”各处输入框为空等情况，点确定，是否会出现异常
        """
        log("测试------《问题反馈》")
        click_ele("我的", "我的")
        click_ele("我的", "问题反馈")
        click_ele("问题反馈", "自助报障")
        click_ele("自助报障", "提交")
        key_del_text("自助报障", "联系人")
        key_del_text("自助报障", "邮箱")
        key_back()
        click_ele("自助报障", "提交")
        assert_ele_is_exist("自助报障", "提交")
        key_back()
        click_ele("问题反馈", "物流")
        click_ele("物流", "提交")
        key_del_text("物流", "联系人")
        key_del_text("物流", "邮箱")
        key_back()
        click_ele("物流", "提交")
        assert_ele_is_exist("物流", "提交")
        key_back()
        click_ele("问题反馈", "客服问题")
        click_ele("客服问题", "提交")
        key_del_text("客服问题", "联系人")
        key_del_text("客服问题", "邮箱")
        key_back()
        click_ele("客服问题", "提交")
        assert_ele_is_exist("客服问题", "提交")
        key_back()
        click_ele("问题反馈", "BLUETTI APP")
        click_ele("BLUETTI APP", "提交")
        key_del_text("BLUETTI APP", "联系人")
        key_del_text("BLUETTI APP", "邮箱")
        key_back()
        click_ele("BLUETTI APP", "提交")
        assert_ele_is_exist("BLUETTI APP", "提交")
        key_back(2)

    def test_clear_cache(self):
        """
        测试清理缓存
        """
        log("测试------《清理缓存》")
        click_ele("我的", "我的")
        swipe_bottom_top()
        click_ele("我的", "清理缓存")
        cache_data = get_ele_text("清理缓存", "缓存数据量")
        click_ele("通用", "确定")
        if cache_data == "0.0M":
            assert_ele_is_exist("我的", "清理缓存")
        else:
            click_ele("我的", "清理缓存")
            assert_ele_text("清理缓存", "缓存数据量", "0.0M")

    def test_sign(self):
        """
        测试签到
        """
        log("测试------《签到》")
        click_ele("我的", "我的")
        swipe_bottom_top()
        click_ele("我的", "签到")
        sign_text = get_ele_text("签到", "签到")
        click_ele("签到", "签到")
        if sign_text == "已签到":
            assert_ele_is_exist("签到", "积分")
        else:
            assert_ele_text("签到", "签到","已签到")

    def test_installer(self):
        """
        安装商跳转联系我们
        """
        log("测试------《安装商跳转联系我们》")
        click_ele("我的", "我的")
        click_ele("我的", "安装商")
        click_ele("安装商", "联系我们")
        assert_ele_is_exist("联系我们", "电话服务")
        key_back(2)