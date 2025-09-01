import unittest

from common_android.assert_methods import *
from common_android.app_operation import *
from common_android.basic_operation import *
from utils.adb_command import filter_logcat


class TestUniversal(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ST.SAVE_IMAGE = False
        log("------测试类前置处理------")
        cls.app = "net.poweroak.bluetticloud"
        start_app(cls.app)
        login_by_mail("us")
        switch_lang()

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

    def test_me_main_page(self):
        """
        我的
        """
        log("测试------《我的》")
        click_ele("我的", "我的")
        assert_ele_is_exist("我的", "我的账户")
        swipe_universal(0.5, 0.8, 0.5, 0.2)
        assert_ele_is_exist("我的", "订阅品牌")

    def test_me_push(self):
        """
        我的-push
        """
        log("测试------《我的-push》")
        click_ele("我的", "我的")
        click_ele("我的", "push入口")
        assert_ele_is_exist("push消息列表", "我的消息")
        swipe_bottom_top()
        click_ele("push消息列表", "设置")
        assert_ele_is_exist("push消息设置", "设备通知")

    def test_me_loyalty_program(self):
        """
        我的-loyalty_program
        """
        log("测试------《我的-loyalty_program》")
        click_ele("我的", "我的")
        click_ele("我的", "忠诚度计划")
        assert_ele_is_exist("忠诚度计划", "标题")
        click_ele("忠诚度计划", "签到")
        assert_ele_is_exist("签到", "签到")
        click_back_button()
        click_ele("忠诚度计划", "积分商城")
        assert_ele_is_exist("积分商城", "积分商品")
        click_back_button()
        click_ele("忠诚度计划", "获得X项权益")
        assert_ele_is_exist("权益等级", "标题")
        click_back_button()
        swipe_universal(0.5, 0.8, 0.5, 0.3)
        assert_ele_is_exist("忠诚度计划", "标题")
        click_ele("忠诚度计划", "历史记录")
        assert_ele_is_exist("历史记录", "标题")
        click_back_button(2)

    def test_me_my_account(self):
        """
        我的-我的账户
        """
        log("测试------《我的-我的账户》")
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

    def test_me_address(self):
        """
        我的-地址管理
        """
        log("测试------《我的-地址管理》")
        click_ele("我的", "我的")
        click_ele("我的", "地址管理")
        assert_ele_is_exist("地址管理", "新增地址")
        click_ele("地址管理", "新增地址")
        assert_ele_is_exist("新增地址", "名字")
        swipe_universal(0.5, 0.9, 0.5, 0.2, num=2)
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

    def test_me_bluetti_star(self):
        """
        我的-BLUETTI STAR
        """
        log("测试------《我的-BLUETTI STAR》")
        click_ele("我的", "我的")
        click_ele("我的", "BLUETTI STAR")
        sleep()
        assert_ele_is_exist("BLUETTI STAR", "BLUETTI STAR")
        for i in range(5):
            swipe_universal(0.5, 0.7, 0.5, 0.2)
            assert_ele_is_exist("BLUETTI STAR", "BLUETTI STAR")

    def test_me_installer(self):
        """
        我的-安装商
        """
        log("测试------《我的-安装商》")
        click_ele("我的", "我的")
        click_ele("我的", "安装商")
        assert_ele_is_exist("安装商", "安装商")
        for i in range(2):
            swipe_universal(0.5, 0.7, 0.5, 0.2)
            assert_ele_is_exist("安装商", "安装商")
        click_ele("安装商", "联系我们")
        assert_ele_is_exist("联系我们", "电话服务")
        click_back_button(2)

    def test_me_referral_rewards(self):
        """
        我的-引荐计划
        """
        log("测试------《我的-引荐计划》")
        click_ele("我的", "我的")
        click_ele("我的", "引荐计划")
        sleep(3)
        assert_ele_is_exist("引荐计划", "标题")
        click_ele("引荐计划", "Refer order")
        assert_ele_is_exist("Refer order", "标题")
        click_back_button()
        click_ele("引荐计划", "你的朋友")
        assert_ele_is_exist("引荐计划", "标题")
        click_ele("引荐计划", "你的")
        for i in range(3):
            swipe_universal(0.5, 0.7, 0.5, 0.3)
            assert_ele_is_exist("引荐计划", "标题")
        click_back_button()

    def test_me_app_mark(self):
        """
        我的-app评分
        """
        log("测试------《我的-app评分》")
        click_ele("我的", "App评分")
        assert_ele_is_exist("我的", "地址管理", is_exist=False)
        home()
        start_app(self.app)

    def test_me_feedback(self):
        """
        我的-问题反馈
        """
        log("测试------《我的-问题反馈》")
        click_ele("我的", "我的")
        swipe_universal(0.5, 0.8, 0.5, 0.2)
        click_ele("我的", "问题反馈")
        wait_for_ele("问题反馈", "自助报障")
        assert_ele_is_exist("问题反馈", "物流")
        click_ele("问题反馈", "自助报障")
        assert_ele_is_exist("自助报障", "提交")
        click_ele("自助报障", "设备序列号")
        assert_ele_is_exist("自助报障", "标题")
        click_ele("自助报障", "设备型号-请选择")
        assert_ele_is_exist("设备型号", "设备型号")
        for i in range(9):
            swipe_universal(0.5, 0.7, 0.5, 0.3)
            assert_ele_is_exist("设备型号", "设备型号")
        click_ele("设备型号", "关闭按钮")
        click_ele("自助报障", "国家地区")
        assert_ele_is_exist("国家地区", "搜索框")
        click_back_button()
        for i in range(4):
            swipe_universal(0.5, 0.7, 0.5, 0.2)
            assert_ele_is_exist("自助报障", "提交")
        click_ele("自助报障", "提交")
        assert_ele_is_exist("自助报障", "提交")
        click_ele("自助报障", "照片")
        assert_ele_is_exist("自助报障", "提交", False)
        key_back()
        click_back_button()
        click_ele("问题反馈", "物流")
        assert_ele_is_exist("物流", "标题")
        swipe_universal(0.5, 0.7, 0.5, 0.3)
        assert_ele_is_exist("物流", "标题")
        click_ele("物流", "提交")
        assert_ele_is_exist("物流", "标题")
        click_back_button()
        click_ele("问题反馈", "客服问题")
        assert_ele_is_exist("客服问题", "提交")
        for i in range(4):
            swipe_universal(0.5, 0.7, 0.5, 0.3)
            assert_ele_is_exist("客服问题", "提交")
        click_ele("客服问题", "提交")
        assert_ele_is_exist("客服问题", "提交")
        click_back_button()
        click_ele("问题反馈", "BLUETTI APP")
        assert_ele_is_exist("BLUETTI APP", "提交")
        swipe_universal(0.5, 0.7, 0.5, 0.3)
        assert_ele_is_exist("BLUETTI APP", "提交")
        click_ele("BLUETTI APP", "提交")
        assert_ele_is_exist("BLUETTI APP", "提交")
        click_back_button()

    def test_me_sign(self):
        """
        我的-签到
        """
        log("测试------《我的-签到》")
        click_ele("我的", "我的")
        swipe_universal(0.5, 0.8, 0.5, 0.2)
        click_ele("我的", "签到")
        sign_text = get_ele_text("签到", "签到")
        coins_text = get_ele_text("签到", "积分")
        click_ele("签到", "签到")
        assert_ele_is_exist("签到", "签到")
        if sign_text == "已签到":
            assert_ele_text("签到", "积分", coins_text)
        else:
            click_back_button()  #其实不用这一步，点击签到，积分就应该改变，增加容错性，不影响测试结果
            click_ele("我的", "签到")  #其实不用这一步，点击签到，积分就应该改变，增加容错性，不影响测试结果
            assert_ele_text("签到", "签到", "已签到")
            assert_ele_text("签到", "积分", coins_text, False)
        click_ele("签到", "签到规则")
        assert_ele_is_exist("签到规则", "签到规则")
        click_back_button()
        click_ele("签到", "积分")
        assert_ele_is_exist("我的积分", "积分明细")
        click_ele("我的积分", "兑换记录")
        assert_ele_is_exist("我的积分", "兑换记录")
        click_back_button()
        click_ele("签到", "等级")
        assert_ele_is_exist("权益等级", "标题")
        swipe_universal(0.8, 0.25, 0.2, 0.25)
        assert_ele_is_exist("权益等级", "等级2")
        click_ele("权益等级", "等级说明")
        assert_ele_is_exist("等级说明", "标题")
        for i in range(2):
            swipe_universal(0.5, 0.8, 0.5, 0.2)
            assert_ele_is_exist("等级说明", "标题")
        click_back_button(3)

    def test_me_lottery(self):
        """
        我的-大转盘
        """
        log("测试------《我的-大转盘》")
        click_ele("我的", "我的")
        swipe_universal(0.5, 0.8, 0.5, 0.2)
        click_ele("我的", "大转盘")
        assert_ele_is_exist("大转盘", "大转盘活动")
        swipe_universal(0.5, 0.6, 0.5, 0.3)
        assert_ele_is_exist("大转盘", "大转盘活动")
        click_ele("大转盘", "右上角按钮")
        assert_ele_is_exist("大转盘", "活动规则")
        click_ele("大转盘", "我的记录")
        assert_ele_is_exist("我的记录", "中奖记录")
        key_back()  #应该使用click_back_button()，此处有bug
        click_ele("大转盘", "右上角按钮")
        click_ele("大转盘", "活动规则")
        assert_ele_is_exist("活动规则", "活动规则")
        for i in range(5):
            swipe_universal(0.5, 0.8, 0.5, 0.2)
            assert_ele_is_exist("活动规则", "活动规则")
        key_back(2)  #应该使用click_back_button(2)，此处有bug

    def test_me_clear_cache(self):
        """
        我的-清理缓存
        """
        log("测试------《我的-清理缓存》")
        click_ele("我的", "我的")
        swipe_universal(0.5, 0.8, 0.5, 0.2)
        click_ele("我的", "清理缓存")
        cache_data = get_ele_text("清理缓存", "缓存数据量")
        click_ele("通用", "确定")
        if cache_data == "0.0M":
            assert_ele_is_exist("我的", "清理缓存")
        else:
            click_ele("我的", "清理缓存")
            assert_ele_text("清理缓存", "缓存数据量", "0.0M")

    def test_me_user_agreement(self):
        """
        我的-用户协议
        """
        log("测试------《我的-用户协议》")
        click_ele("我的", "我的")
        swipe_universal(0.5, 0.8, 0.5, 0.2)
        click_ele("我的", "用户协议")
        assert_ele_is_exist("用户协议", "用户服务协议")
        for i in range(34):
            swipe_universal(0.5, 0.8, 0.5, 0.2)
            assert_ele_is_exist("用户协议", "用户服务协议")
        click_back_button()

    def test_me_privacy_policy(self):
        """
        我的-隐私政策
        """
        log("测试------《我的-隐私政策》")
        click_ele("我的", "我的")
        swipe_universal(0.5, 0.8, 0.5, 0.2)
        click_ele("我的", "隐私政策")
        assert_ele_is_exist("隐私政策", "隐私政策")
        for i in range(20):
            swipe_universal(0.5, 0.8, 0.5, 0.2)
            assert_ele_is_exist("隐私政策", "隐私政策")
        click_back_button()

    def test_me_setting(self):
        """
        我的-通用设置
        """
        log("测试------《我的-通用设置》")
        click_ele("我的", "我的")
        swipe_universal(0.5, 0.8, 0.5, 0.2)
        click_ele("我的", "通用设置")
        assert_ele_is_exist("通用设置", "多语言")
        click_ele("通用设置", "多语言")
        assert_ele_is_exist("通用", "确定")
        for i in range(2):
            swipe_universal(0.5, 0.7, 0.5, 0.3)
            assert_ele_is_exist("通用", "确定")
        click_ele("多语言", "关闭按钮")
        click_ele("通用设置", "字体大小")
        assert_ele_is_exist("字体大小", "大")
        click_ele("字体大小", "关闭按钮")
        click_ele("通用设置", "主题模式")
        assert_ele_is_exist("主题模式", "深色模式")
        click_ele("主题模式", "关闭按钮")
        click_ele("通用设置", "时区")
        assert_ele_is_exist("时区", "搜索框")
        for i in range(34):
            swipe_universal(0.5, 0.8, 0.5, 0.2)
            assert_ele_is_exist("时区", "搜索框")
        input_text("时区", "搜索框", "美国")
        assert_ele_is_exist("时区", "搜索框", False)
        select_data("America/New_York")
        assert_ele_is_exist("通用设置", "通用设置")
        click_ele("通用设置", "温度单位")
        assert_ele_is_exist("温度单位", "温度单位")
        click_ele("温度单位", "关闭按钮")
        click_ele("通用设置", "货币单位")
        assert_ele_is_exist("货币单位", "搜索框")
        for i in range(25):
            swipe_universal(0.5, 0.8, 0.5, 0.2)
            assert_ele_is_exist("货币单位", "搜索框")
        input_text("货币单位", "搜索框", "美国")
        sleep()
        assert_ele_is_exist("货币单位", "搜索按钮")
        select_data("USD")
        assert_ele_is_exist("通用设置", "通用设置")
        click_ele("通用设置", "电价设置")
        assert_ele_is_exist("电价设置", "电价设置方式")
        click_ele("电价设置", "电价设置方式")
        assert_ele_is_exist("电价设置", "固定电价")
        click_ele("电价设置", "固定电价")
        assert_ele_is_exist("通用", "确定")
        click_ele("固定电价", "买电电价")
        assert_ele_is_exist("通用", "确定")
        click_ele("固定电价", "货币单位")
        assert_ele_is_exist("货币单位", "搜索框")
        click_back_button()
        assert_ele_is_exist("通用", "确定")
        click_ele("固定电价", "电价输入框")
        assert_ele_is_exist("通用", "确定")
        click_ele("固定电价", "关闭按钮")
        click_ele("固定电价", "售电电价")
        assert_ele_is_exist("通用", "确定")
        click_ele("固定电价", "货币单位")
        assert_ele_is_exist("货币单位", "搜索框")
        click_back_button()
        assert_ele_is_exist("通用", "确定")
        click_ele("固定电价", "电价输入框")
        assert_ele_is_exist("通用", "确定")
        click_ele("固定电价", "关闭按钮")
        click_back_button()
        click_ele("电价设置", "峰谷电价")
        click_ele("峰谷电价", "波峰时间")
        click_ele("通用", "确定")
        assert_ele_is_exist("通用", "确定")
        click_ele("峰谷电价", "关闭按钮")
        click_ele("峰谷电价", "波谷时间")
        assert_ele_is_exist("通用", "确定")
        click_back_button(3)
        click_ele("通用设置", "碳排量系数")
        assert_ele_is_exist("碳排量系数", "输入框")
        click_ele("碳排量系数", "输入框")
        assert_ele_is_exist("通用", "确定")
        click_ele("碳排量系数", "碳排量系数说明")
        assert_ele_is_exist("碳排量系数说明", "关闭按钮")
        click_ele("碳排量系数说明", "关闭按钮")
        click_ele("碳排量系数", "关闭按钮")
        click_ele("通用设置", "数据统计服务")
        assert_ele_is_exist("数据统计服务", "数据统计服务")
        click_ele("数据统计服务", "授权")
        assert_ele_is_exist("数据统计服务", "取消授权")
        click_back_button()
        click_ele("通用设置", "数据统计服务")
        assert_ele_is_exist("数据统计服务", "取消授权")
        click_ele("数据统计服务", "取消授权")
        assert_ele_is_exist("通用", "确定")
        click_ele("通用", "取消")
        assert_ele_is_exist("数据统计服务", "取消授权")
        click_ele("数据统计服务", "取消授权")
        assert_ele_is_exist("通用", "确定")
        click_ele("通用", "确定")
        assert_ele_is_exist("数据统计服务", "数据统计服务")
        click_back_button()

    def test_me_subscribe(self):
        """
        我的-订阅品牌
        """
        log("测试------《我的-订阅品牌》")
        click_ele("我的", "我的")
        swipe_universal(0.5, 0.8, 0.5, 0.2)
        click_ele("我的", "订阅品牌")
        assert_ele_is_exist("订阅品牌", "确认订阅")
        for i in range(3):
            swipe_universal(0.5, 0.7, 0.5, 0.2)
            assert_ele_is_exist("订阅品牌", "确认订阅")
        click_ele("订阅品牌", "确认订阅")
        assert_ele_is_exist("订阅品牌", "确认订阅")
        click_ele("订阅品牌", "取消订阅")
        assert_ele_is_exist("订阅品牌", "确认订阅")
        click_back_button()

    def test_service_main_page(self):
        """
        服务
        """
        log("测试------《服务》")
        click_ele("服务", "服务")
        assert_ele_is_exist("服务", "常见问题")

    def test_service_faq(self):
        """
        服务-常见问题
        """
        log("测试------《服务-常见问题》")
        click_ele("服务", "服务")
        click_ele("服务", "常见问题")
        wait_for_ele("常见问题", "美国")
        assert_ele_is_exist("常见问题", "搜索")
        click_ele("常见问题", "搜索")
        assert_ele_is_exist("搜索", "国家")
        click_ele("搜索", "国家")
        assert_ele_is_exist("搜索", "请选择")
        swipe_universal(0.5, 0.9, 0.5, 0.7)
        assert_ele_is_exist("搜索", "请选择")
        swipe_universal(0.5, 0.7, 0.5, 0.9)
        assert_ele_is_exist("搜索", "请选择")
        click_ele("搜索", "美国")
        assert_ele_is_exist("搜索", "请选择")
        click_ele("搜索", "日本")
        assert_ele_is_exist("搜索", "国家")
        click_ele("搜索", "国家")
        click_ele("搜索", "美国")
        click_ele("搜索", "国家")
        click_ele("搜索", "国家关闭按钮")
        input_text("搜索", "搜索框", "20")
        assert_ele_is_exist("搜索", "国家")
        sleep()
        input_text("搜索", "搜索框", "300")
        sleep()
        assert_ele_is_exist("搜索", "国家")
        click_ele("搜索", "AC200+B300")
        assert_ele_is_exist("问题列表", "问题")
        click_back_button()
        input_text("搜索", "搜索框", "文章1")
        sleep()
        assert_ele_is_exist("搜索", "国家")
        click_ele("搜索", "详情")
        sleep()
        assert_ele_is_exist("详情", "详情")
        click_back_button()
        click_ele("搜索", "AC200+B300")
        assert_ele_is_exist("问题列表", "问题")
        click_back_button(2)
        click_ele("常见问题", "国家")
        assert_ele_is_exist("搜索", "请选择")
        click_ele("搜索", "国家关闭按钮")
        click_ele("常见问题", "AC200+B300")
        click_ele("问题列表", "搜索")
        assert_ele_is_exist("搜索", "国家")
        click_back_button()
        click_ele("问题列表", "详情")
        assert_ele_is_exist("商品详情", "商品详情")
        click_ele("商品详情", "返回按钮")
        click_ele("问题列表", "问题")
        assert_ele_is_exist("详情", "详情")
        click_ele("详情", "AC200+B300")
        assert_ele_is_exist("问题列表", "详情")
        click_back_button()
        assert_ele_is_exist("常见问题", "AC200+B300")
        click_ele("常见问题", "AC200+B300")
        click_ele("问题列表", "问题")
        for i in range(2):
            click_ele("详情", "已解决")
            assert_ele_is_exist("问题列表", "详情")
            sleep()
        click_ele("详情", "未解决")
        assert_ele_is_exist("详情", "问题反馈")
        click_ele("详情", "问题反馈")
        sleep()
        assert_ele_is_exist("问题反馈", "自助报障")
        click_back_button()
        click_ele("详情", "已解决")
        sleep()
        click_ele("详情", "未解决")
        click_ele("详情", "联系我们")
        assert_ele_is_exist("联系我们", "电话服务")
        click_back_button(4)

    def test_service_feedback(self):
        """
        服务-问题反馈
        """
        log("测试------《问题反馈》")
        click_ele("服务", "服务")
        click_ele("服务", "问题反馈")
        assert_ele_is_exist("问题反馈", "自助报障")
        click_back_button()

    def test_service_guidelines(self):
        """
        服务-用户指引
        """
        log("测试------《用户指引》")
        click_ele("服务", "服务")
        click_ele("服务", "用户指引")
        assert_ele_is_exist("用户指引", "标题")
        click_ele("用户指引", "AC系列指南")
        assert_ele_is_exist("用户指引", "标题")
        click_ele("用户指引", "太阳能板指南")
        click_ele("用户指引", "分类列表")
        assert_ele_is_exist("用户指引", "全部分类")
        click_ele("用户指引", "分类列表")
        click_ele("用户指引", "PV200")
        assert_ele_is_exist("用户指引", "标题")
        click_ele("用户指引", "PV420")
        click_ele("用户指引", "问题1")
        assert_ele_is_exist("用户指引", "标题")
        click_ele("用户指引", "用户手册")
        sleep()
        assert_ele_is_exist("用户手册", "国家地区")
        click_ele("用户手册", "搜索")
        assert_ele_is_exist("用户手册", "国家")
        click_ele("用户手册", "国家")
        assert_ele_is_exist("用户手册", "US")
        click_ele("用户手册", "CN")
        assert_ele_is_exist("用户手册", "国家")
        click_ele("用户手册", "国家")
        click_ele("用户手册", "US")
        assert_ele_is_exist("用户手册", "国家")
        click_ele("用户手册", "国家")
        click_ele("用户手册", "关闭按钮")
        input_text_enter("用户手册", "搜索框", "600")
        assert_ele_is_exist("用户手册", "EP600")
        click_ele("用户手册", "EP600")
        assert_ele_is_exist("EP600", "用户手册")
        click_back_button(2)
        click_ele("用户手册", "国家地区")
        assert_ele_is_exist("用户手册", "请选择")
        click_ele("用户手册", "中国")
        assert_ele_is_exist("用户手册", "国家地区")
        click_ele("用户手册", "国家地区")
        click_ele("用户手册", "美国")
        click_ele("用户手册", "国家地区")
        click_ele("用户手册", "关闭按钮")
        assert_ele_is_exist("用户手册", "EP600")
        click_ele("用户手册", "EP600")
        click_ele("EP600", "附件列表")
        assert_ele_is_exist("EP600", "用户手册")
        click_ele("EP600", "图片")
        assert_ele_is_exist("EP600", "用户手册", False)
        home()
        start_app(self.app)
        click_ele("EP600", "PDF")
        assert_ele_is_exist("EP600", "文件预览")
        click_ele("EP600", "下载")
        assert_ele_is_exist("EP600", "用户手册", False)
        home()
        start_app(self.app)
        click_back_button()
        click_ele("EP600", "用户手册")
        assert_ele_is_exist("EP600", "用户手册")
        click_ele("EP600", "附件列表")
        click_ele("EP600", "excel文件")
        assert_ele_is_exist("EP600", "用户手册", False)
        home()
        start_app(self.app)
        click_ele("EP600", "视频文件")
        assert_ele_is_exist("EP600", "用户手册", False)
        home()
        start_app(self.app)
        click_ele("EP600", "图片文件")
        assert_ele_is_exist("EP600", "用户手册", False)
        home()
        start_app(self.app)
        click_back_button(3)

    def test_service_trouble_shooting(self):
        """
        服务-故障排查
        """
        log("测试------《故障排查》")
        click_ele("服务", "服务")
        click_ele("服务", "故障排查")
        wait_for_ele("常见问题", "美国")
        assert_ele_is_exist("常见问题", "搜索")
        click_ele("常见问题", "搜索")
        assert_ele_is_exist("搜索", "国家")
        click_ele("搜索", "国家")
        assert_ele_is_exist("搜索", "请选择")
        swipe_universal(0.5, 0.9, 0.5, 0.7)
        assert_ele_is_exist("搜索", "请选择")
        swipe_universal(0.5, 0.7, 0.5, 0.9)
        assert_ele_is_exist("搜索", "请选择")
        click_ele("搜索", "美国")
        assert_ele_is_exist("搜索", "请选择")
        click_ele("搜索", "中国")
        assert_ele_is_exist("搜索", "国家")
        click_ele("搜索", "国家")
        click_ele("搜索", "美国")
        click_ele("搜索", "国家")
        click_ele("搜索", "国家关闭按钮")
        input_text("搜索", "搜索框", "20")
        assert_ele_is_exist("搜索", "国家")
        sleep()
        input_text("搜索", "搜索框", "500C")
        sleep()
        assert_ele_is_exist("搜索", "国家")
        click_ele("搜索", "BC500C")
        assert_ele_is_exist("问题列表", "BC500C")
        click_back_button()
        input_text("搜索", "搜索框", "123")
        sleep()
        assert_ele_is_exist("搜索", "国家")
        click_ele("搜索", "详情")
        sleep()
        assert_ele_is_exist("详情", "已解决")
        click_back_button()
        click_ele("搜索", "BC500C")
        assert_ele_is_exist("问题列表", "BC500C")
        click_back_button(2)
        click_ele("常见问题", "国家")
        assert_ele_is_exist("搜索", "请选择")
        click_ele("搜索", "国家关闭按钮")
        click_ele("常见问题", "BC500C")
        click_ele("问题列表", "搜索")
        assert_ele_is_exist("搜索", "国家")
        click_back_button()
        click_ele("问题列表", "Charging")
        assert_ele_is_exist("问题列表", "Charging")
        click_ele("问题列表", "General")
        click_ele("问题列表", "123")
        assert_ele_is_exist("详情", "详情")
        click_ele("详情", "BC500C")
        assert_ele_is_exist("问题列表", "General")
        click_back_button()
        assert_ele_is_exist("常见问题", "BC500C")
        click_ele("常见问题", "BC500C")
        click_ele("问题列表", "123")
        for i in range(2):
            click_ele("详情", "已解决")
            assert_ele_is_exist("问题列表", "详情")
            sleep()
        click_ele("详情", "未解决")
        assert_ele_is_exist("详情", "问题反馈")
        click_ele("详情", "问题反馈")
        sleep()
        assert_ele_is_exist("问题反馈", "自助报障")
        click_back_button()
        click_ele("详情", "已解决")
        sleep()
        click_ele("详情", "未解决")
        click_ele("详情", "联系我们")
        assert_ele_is_exist("联系我们", "电话服务")
        click_back_button(4)

    def test_service_contact_us(self):
        """
        服务-联系我们
        """
        log("测试------《联系我们》")
        click_ele("服务", "服务")
        click_ele("服务", "联系我们")
        assert_ele_is_exist("联系我们", "在线客服")
        click_ele("联系我们", "常见问题")
        assert_ele_is_exist("联系我们", "在线客服")
        click_ele("联系我们", "服务")
        click_ele("联系我们", "分类")
        assert_ele_is_exist("联系我们", "全部分类")
        click_ele("联系我们", "维修")
        assert_ele_is_exist("联系我们", "在线客服")
        click_ele("联系我们", "退换")
        click_ele("联系我们", "问题1")
        assert_ele_is_exist("联系我们", "在线客服")
        click_ele("联系我们", "在线客服")
        assert_ele_is_exist("联系我们", "标题")
        click_back_button()
        click_ele("联系我们", "电话服务")
        assert_ele_is_exist("联系我们", "电话服务")
        click_ele("联系我们", "电话")
        click_ele("联系我们", "关闭按钮")
        click_ele("联系我们", "电话")
        assert_ele_is_exist("联系我们", "电话")
        click_ele("联系我们", "复制")
        assert_ele_is_exist("联系我们", "电话")
        click_ele("联系我们", "电话")
        click_ele("联系我们", "拨打")
        assert_ele_is_exist("联系我们", "电话服务", False)
        home()
        start_app(self.app)
        for i in range(3):
            swipe_universal(0.5, 0.8, 0.5, 0.2)
            assert_ele_is_exist("联系我们", "电话服务")
        click_back_button()
        click_ele("联系我们", "邮箱服务")
        assert_ele_is_exist("联系我们", "邮箱服务")
        click_ele("联系我们", "邮箱")
        click_ele("联系我们", "关闭按钮")
        click_ele("联系我们", "邮箱")
        assert_ele_is_exist("联系我们", "邮箱")
        click_ele("联系我们", "复制")
        assert_ele_is_exist("联系我们", "邮箱")
        click_ele("联系我们", "邮箱")
        click_ele("联系我们", "写邮件")
        assert_ele_is_exist("联系我们", "邮箱服务", False)
        home()
        start_app(self.app)
        for i in range(3):
            swipe_universal(0.5, 0.8, 0.5, 0.2)
            assert_ele_is_exist("联系我们", "邮箱服务")
        click_back_button()

    def test_service_trade_in(self):
        """
        服务-以旧换新
        """
        log("测试------《以旧换新》")
        click_ele("服务", "服务")
        click_ele("服务", "以旧换新")
        assert_ele_is_exist("以旧换新", "标题")
        click_ele("以旧换新", "免费评估")
        click_ele("以旧换新", "下一步")
        assert_ele_is_exist("以旧换新", "下一步")
        click_back_button()
        click_ele("以旧换新", "最高抵扣")
        assert_ele_is_exist("以旧换新", "下一步")
        click_back_button()
        click_ele("以旧换新", "问题1")
        assert_ele_is_exist("以旧换新", "标题")
        for i in range(4):
            swipe_universal(0.5, 0.8, 0.5, 0.2)
            assert_ele_is_exist("以旧换新", "标题")

    def test_service_installation(self):
        """
        服务-安装
        """
        log("测试------《安装》")
        click_ele("服务", "服务")
        swipe_universal(0.5, 0.8, 0.5, 0.2)
        click_ele("服务", "安装")
        assert_ele_is_exist("安装", "标题")
        click_ele("安装", "记录")
        assert_ele_is_exist("处理进度", "标题")
        click_back_button()
        click_ele("安装", "安装信息选择")
        assert_ele_is_exist("地址管理", "新增地址")
        click_back_button()
        click_ele("安装", "型号选择")
        assert_ele_is_exist("通用", "确定")
        click_ele("通用", "确定")
        assert_ele_is_exist("安装", "标题")
        click_ele("通用", "下一步")
        assert_ele_is_exist("安装", "标题")
        click_back_button()

    def test_service_maintenance(self):
        """
        服务-维修
        """
        log("测试------《维修》")
        click_ele("服务", "服务")
        swipe_universal(0.5, 0.8, 0.5, 0.2)
        click_ele("服务", "维修")
        assert_ele_is_exist("维修", "标题")

    def test_service_progress(self):
        """
        服务-处理进度
        """
        log("测试------《处理进度》")
        click_ele("服务", "服务")
        swipe_universal(0.5, 0.8, 0.5, 0.2)
        click_ele("服务", "处理进度")
        assert_ele_is_exist("处理进度", "标题")
        click_ele("处理进度", "维修")
        assert_ele_is_exist("处理进度", "标题")

    def test_service_warranty(self):
        """
        服务-保修政策
        """
        log("测试------《保修政策》")
        click_ele("服务", "服务")
        swipe_universal(0.5, 0.8, 0.5, 0.2)
        click_ele("服务", "保修政策")
        assert_ele_is_exist("保修政策", "标题")

    def test_service_refund(self):
        """
        服务-退款政策
        """
        log("测试------《退款政策》")
        click_ele("服务", "服务")
        swipe_universal(0.5, 0.8, 0.5, 0.2)
        click_ele("服务", "退款政策")
        assert_ele_is_exist("退款政策", "标题")

    def test_service_register_product(self):
        """
        服务-产品登记
        """
        log("测试------《产品登记》")
        click_ele("服务", "服务")
        swipe_universal(0.5, 0.8, 0.5, 0.2)
        click_ele("服务", "产品登记")
        assert_ele_is_exist("产品登记", "标题")

    def test_service_extend_warranty(self):
        """
        服务-延保服务
        """
        log("测试------《延保服务》")
        click_ele("服务", "服务")
        swipe_universal(0.5, 0.8, 0.5, 0.2)
        click_ele("服务", "延保服务")
        assert_ele_is_exist("延保服务", "标题")

    def test_community_main_page(self):
        """
        社区
        """
        log("测试------《社区》")
        click_ele("社区", "社区")
        assert_ele_is_exist("社区", "消息")
        pass
        for i in range(5):
            swipe_universal(0.5,0.7,0.5,0.2)
            assert_ele_is_exist("社区", "头像")

    def test_community_user_center(self):
        """
        社区-用户中心
        """
        log("测试------《社区-用户中心》")
        click_ele("社区", "社区")
        pass

    def test_community_search(self):
        """
        社区-搜索
        """
        log("测试------《社区-搜索》")
        click_ele("社区", "社区")
        pass

    def test_community_message(self):
        """
        社区-消息
        """
        log("测试------《社区-消息》")
        click_ele("社区", "社区")
        pass

    def test_community_event(self):
        """
        社区-event
        """
        log("测试------《社区-event》")
        click_ele("社区", "社区")
        pass

    def test_community_cocreate(self):
        """
        社区-cocreate
        """
        log("测试------《社区-cocreate》")
        click_ele("社区", "社区")
        pass

    def test_community_life(self):
        """
        社区-life
        """
        log("测试------《社区-life》")
        click_ele("社区", "社区")
        pass

    def test_community_news(self):
        """
        社区-news
        """
        log("测试------《社区-news》")
        click_ele("社区", "社区")
        pass

    def test_home_main_page(self):
        """
        首页
        """
        log("测试------《首页》")
        click_ele("首页", "首页")
        assert_ele_is_exist("首页", "天气")
        swipe_universal(0.5, 0.8, 0.5, 0.1)
        assert_ele_is_exist("首页", "用户指引")

    def test_home_weather(self):
        """
        首页-天气
        """
        log("测试------《首页-天气》")
        click_ele("首页", "首页")
        click_ele("首页", "天气")
        assert_ele_is_exist("首页", "天气关闭按钮")
        click_ele("首页", "天气关闭按钮")

    def test_home_calculator(self):
        """
        首页-选型推荐
        """
        log("测试------《首页-选型推荐》")
        click_ele("首页", "首页")
        click_ele("首页", "选型推荐")
        assert_ele_is_exist("首页", "选型推荐")
        for i in range(4):
            swipe_universal(0.5, 0.8, 0.5, 0.1)
            assert_ele_is_exist("首页", "选型推荐")
        click_back_button()

    def test_home_laaf(self):
        """
        首页-LAAF
        """
        log("测试------《首页-LAAF》")
        click_ele("首页", "首页")
        click_ele("首页", "LAAF")
        assert_ele_is_exist("LAAF", "标题")
        click_ele("LAAF", "LAAF说明")
        assert_ele_is_exist("LAAF", "LAAF说明标题")
        click_back_button(2)

    def test_home_contact_us(self):
        """
        首页-联系我们
        """
        log("测试------《首页-联系我们》")
        click_ele("首页", "首页")
        swipe_universal(0.5, 0.8, 0.5, 0.1)
        click_ele("首页", "联系我们")
        assert_ele_is_exist("联系我们", "电话服务")
        click_back_button()

    def test_home_about_bluetti(self):
        """
        首页-关于我们
        """
        log("测试------《首页-关于我们》")
        click_ele("首页", "首页")
        swipe_universal(0.5, 0.8, 0.5, 0.1)
        click_ele("首页", "关于我们")
        assert_ele_is_exist("关于我们", "标题")
        for i in range(4):
            swipe_universal(0.5, 0.8, 0.5, 0.1)
            assert_ele_is_exist("关于我们", "标题")
        click_back_button()

    def test_home_guidelines(self):
        """
        首页-用户指引
        """
        log("测试------《首页-用户指引》")
        click_ele("首页", "首页")
        swipe_universal(0.5, 0.8, 0.5, 0.1)
        click_ele("首页", "用户指引")
        assert_ele_is_exist("用户指引", "标题")
        click_back_button()

    def test_home_how_to_use(self):
        """
        首页-how to use
        """
        log("测试------《首页-how to use》")
        click_ele("首页", "首页")
        swipe_universal(0.5, 0.8, 0.5, 0.1)
        click_ele("首页", "How-To-Use")
        assert_ele_is_exist("How-To-Use", "标题")
        swipe_universal(0.5, 0.8, 0.5, 0.1)
        assert_ele_is_exist("How-To-Use", "标题")
        click_ele("How-To-Use", "搜索")
        assert_ele_is_exist("How-To-Use", "搜索框")
        click_back_button()
        swipe_universal(0.5, 0.2, 0.5, 0.8)
        click_ele("How-To-Use", "一级标题")
        assert_ele_is_exist("How-To-Use", "二级标题1")
        click_ele("How-To-Use", "二级标题展开")
        assert_ele_is_exist("How-To-Use", "二级标题1")
        click_ele("How-To-Use", "二级标题展开")
        for i in range(5):
            swipe_universal(0.5, 0.8, 0.5, 0.3)
            assert_ele_is_exist("How-To-Use", "二级标题1")
        click_ele("How-To-Use", "搜索")
        input_text_enter("How-To-Use", "搜索框", "simon-test091")
        assert_ele_is_exist("How-To-Use", "搜索标题")
        click_ele("How-To-Use", "视频描述展开")
        assert_ele_is_exist("How-To-Use", "搜索标题")
        click_ele("How-To-Use", "视频1")
        assert_ele_is_exist("通用", "返回按钮")
        click_back_button(2)
        click_ele("How-To-Use", "搜索")
        input_text_enter("How-To-Use", "搜索框", "725mp4视频 成")
        assert_ele_is_exist("How-To-Use", "搜索标题")
        click_ele("How-To-Use", "视频描述展开")
        assert_ele_is_exist("How-To-Use", "搜索标题")
        click_ele("How-To-Use", "视频3")
        assert_ele_is_exist("通用", "返回按钮")
        click_back_button(2)
        click_ele("How-To-Use", "搜索")
        input_text_enter("How-To-Use", "搜索框", "外部链接视频+商")
        assert_ele_is_exist("How-To-Use", "搜索标题")
        click_ele("How-To-Use", "视频描述展开")
        assert_ele_is_exist("How-To-Use", "搜索标题")
        click_ele("How-To-Use", "商品链接")
        sleep()
        assert_ele_is_exist("商品详情", "商品详情")
        key_back()
        click_ele("How-To-Use", "视频描述展开")
        click_ele("How-To-Use", "视频2")
        assert_ele_is_exist("通用", "返回按钮")
        key_back()
        click_back_button(3)
