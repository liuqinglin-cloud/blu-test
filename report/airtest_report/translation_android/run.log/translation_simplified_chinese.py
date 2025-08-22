from common_android.assert_methods import *
from common_android.app_operation import *
from common_android.basic_operation import click_ele
import unittest


class TestSimplifiedChinese(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.lang = "简体中文"
        ST.SAVE_IMAGE = False
        # login_by_mail("us")
        switch_lang(cls.lang)
        log("测试简体中文翻译")
        ST.SAVE_IMAGE = True

    @classmethod
    def tearDownClass(cls):
        ST.SAVE_IMAGE = False
        main_page()
        ST.SAVE_IMAGE = True

    def setUp(self):
        pass

    def tearDown(self):
        ST.SAVE_IMAGE = False
        main_page()
        swipe_top_bottom()
        ST.SAVE_IMAGE = True

    def test_me(self):
        """
        我的
        """
        click_ele("我的", "我的")
        assert_translation_by_find_ele("我的", self.lang)

    def test_my_account(self):
        """
        我的账户
        """
        click_ele("我的", "我的")
        click_ele("我的", "我的账户")
        assert_translation_by_find_ele("我的账户", self.lang)
        click_ele("我的账户", "昵称")
        assert_translation_by_find_ele("修改昵称", self.lang)
        click_ele("通用", "确定")
        click_ele("我的账户", "安全中心")
        assert_translation_by_find_ele("安全中心", self.lang)
        click_ele("安全中心", "安全邮箱")
        assert_translation_by_find_ele("安全邮箱", self.lang)
        key_back()
        click_ele("安全中心", "更改密码")
        assert_translation_by_find_ele("更改密码", self.lang)
        key_back()
        click_ele("安全中心", "google")
        assert_translation_by_find_ele("google账号绑定", self.lang)
        key_back()
        click_ele("安全中心", "twitter")
        assert_translation_by_find_ele("twitter账号绑定", self.lang)
        key_back()
        click_ele("安全中心", "注销账户")
        assert_translation_by_find_ele("注销账户", self.lang)
        key_back(3)

    def test_push(self):
        """
        push
        """
        click_ele("我的", "我的")
        click_ele("我的", "push入口")
        assert_translation_by_find_ele("push消息列表", self.lang)
        click_ele("push消息列表", "设置")
        assert_translation_by_find_ele("push消息设置", self.lang)
        key_back(2)

    def test_address(self):
        """
        地址管理
        """
        click_ele("我的", "我的")
        click_ele("我的", "地址管理")
        assert_translation_by_find_ele("地址管理", self.lang)
        click_ele("地址管理", "新增地址")
        assert_translation_by_find_ele("新增地址", self.lang)
        swipe_top_bottom(num=2)
        swipe_bottom_top()
        click_ele("新增地址", "国家地区")
        assert_translation_by_find_ele("国家地区", self.lang)
        input_text("国家地区", "搜索框", "美国")
        click_ele_for_translation("US")
        click_ele("新增地址", "省州")
        assert_translation_by_find_ele("省州", self.lang)
        key_back(3)

    def test_feedback(self):
        """
        问题反馈
        """
        click_ele("我的", "我的")
        click_ele("我的", "问题反馈")
        assert_translation_by_find_ele("问题反馈", self.lang)
        click_ele("问题反馈", "自助报障")
        assert_translation_by_find_ele("自助报障", self.lang)
        key_back()
        click_ele("问题反馈", "物流")
        assert_translation_by_find_ele("物流", self.lang)
        key_back()
        click_ele("问题反馈", "客服问题")
        assert_translation_by_find_ele("客服问题", self.lang)
        key_back()
        click_ele("问题反馈", "BLUETTI APP")
        assert_translation_by_find_ele("BLUETTI APP", self.lang)
        key_back(2)

    def test_sign(self):
        """
        签到
        """
        click_ele("我的", "我的")
        click_ele("我的", "签到")
        pass

    def test_subscribe(self):
        """
        订阅品牌
        """
        click_ele("我的", "我的")
        swipe_bottom_top()
        click_ele("我的", "订阅品牌")
        sleep()
        text1 = poco("android.widget.LinearLayout").offspring("net.poweroak.bluetticloud.debug:id/cl_content").child(
            "android.webkit.WebView").offspring("app").child("android.view.View").child("android.view.View")[0].child(
            "android.widget.TextView")[2].get_text()
        assert_translation_by_find_ele("订阅品牌", "简体中文服务内容",expectation=text1)
        text2 = poco("android.widget.LinearLayout").offspring("net.poweroak.bluetticloud.debug:id/cl_content").child(
            "android.webkit.WebView").offspring("app").child("android.view.View").child("android.view.View")[0].child(
            "android.widget.TextView")[4].get_text()
        assert_translation_by_find_ele("订阅品牌", "简体中文订阅方式", expectation=text2)
        swipe_bottom_top()
        text3=poco("android.widget.LinearLayout").offspring("net.poweroak.bluetticloud.debug:id/cl_content").child("android.webkit.WebView").offspring("app").child("android.view.View").child("android.view.View")[0].child("android.widget.TextView")[3].get_text()
        assert_translation_by_find_ele("订阅品牌", "简体中文数据保护承诺", expectation=text3)
        swipe_top_bottom()
        assert_translation_by_find_ele("订阅品牌", self.lang)

    def test_setting(self):
        """
        通用设置
        """
        click_ele("我的", "我的")
        swipe_bottom_top()
        click_ele("我的", "通用设置")
        assert_translation_by_find_ele("通用设置", self.lang)
        click_ele("通用设置", "字体大小")
        assert_translation_by_find_ele("字体大小", self.lang)
        click_ele("字体大小", "关闭按钮")
        click_ele("通用设置", "主题模式")
        assert_translation_by_find_ele("主题模式", self.lang)
        click_ele("主题模式", "关闭按钮")
        click_ele("通用设置", "时区")
        assert_translation_by_find_ele("时区", self.lang)
        key_back()
        click_ele("通用设置", "温度单位")
        assert_translation_by_find_ele("温度单位", self.lang)
        click_ele("温度单位", "关闭按钮")
        click_ele("通用设置", "货币单位")
        assert_translation_by_find_ele("货币单位", self.lang)
        key_back()
        click_ele("通用设置", "电价设置")
        assert_translation_by_find_ele("电价设置", self.lang)
        click_ele("电价设置", "电价设置方式")
        assert_translation_by_find_ele("电价设置方式", self.lang)
        click_ele("电价设置", "固定电价")
        assert_translation_by_find_ele("固定电价", self.lang)
        click_ele("固定电价", "买电电价")
        assert_translation_by_find_ele("固定买电电价", self.lang)
        key_back()
        click_ele("固定电价", "售电电价")
        assert_translation_by_find_ele("固定售电电价", self.lang)
        key_back(2)
        click_ele("电价设置", "峰谷电价")
        assert_translation_by_find_ele("峰谷电价", self.lang)
        click_ele("峰谷电价", "波峰时间")
        click_ele("峰谷电价", "关闭按钮")
        click_ele("峰谷电价", "波谷买电电价")
        key_back(4)
        click_ele("通用设置", "碳排量系数")
        assert_translation_by_find_ele("碳排量系数", self.lang)
        click_ele("碳排量系数", "碳排量系数说明")
        assert_translation_by_find_ele("碳排量系数说明", self.lang)
        key_back(2)
        click_ele("通用设置", "数据统计服务")
        assert_translation_by_find_ele("数据统计服务未授权", self.lang)
        click_ele("数据统计服务", "授权")
        assert_translation_by_find_ele("数据统计服务已授权", self.lang)
        click_ele("数据统计服务", "取消授权")
        click_ele("通用", "确定")
        key_back(2)

    def test_privacy_policy(self):
        """
        隐私政策
        """
        click_ele("我的", "我的")
        swipe_bottom_top()
        click_ele("我的", "隐私政策")
        sleep()
        assert_translation_by_find_ele("隐私政策", self.lang)
        key_back()

    def test_user_agreement(self):
        """
        通用设置
        """
        click_ele("我的", "我的")
        swipe_bottom_top()
        click_ele("我的", "用户协议")
        assert_translation_by_find_ele("用户协议", self.lang)



if __name__ == "__main__":
    suite = unittest.TestSuite()
    tests = [TestSimplifiedChinese("test_my_account")]
    suite.addTests(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)
