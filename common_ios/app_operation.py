# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *
from airtest.cli.parser import cli_setup


if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/1C231FDF60050J?cap_method=ADBCAP&touch_method=MAXTOUCH&",])
from poco.drivers.ios import iosPoco
poco = iosPoco()

ST.FIND_TIMEOUT = 20
ST.FIND_TIMEOUT_TMP = 3

def switch_lang_chinese_to_other(lang):
    """
    从简体中文切换至其他语言，传入目标语言即可
    英语："English"
    繁体："繁體中文"
    日语："日本語"
    德语："Deutsch"
    意大利语："Italiano"
    西班牙语："Español"
    法语："Français"
    韩语："한국어"
    乌克兰语："Українська"
    葡萄牙语："Português"
    """
    poco("我的").click()
    poco("通用设置").click()
    poco("多语言").click()
    poco(lang).click()
    poco("确定").click()
    touch(Template(r"tpl1752816903163.png", record_pos=(-0.459, -0.621), resolution=(2048, 2732)))

def switch_lang_other_to_chinese(my,comfirm):
    """
    从其他语言切换至简体中文，传入“我的”翻译文案，选择语言后“确认按钮”的翻译文案
    英语："Me","OK"
    繁体："我的","確定"
    日语："マイページ","はい"
    德语："Mein","Bestätigen"
    意大利语："Io","OK"
    西班牙语："Yo","Aceptar"
    法语："Moi","OK"
    韩语："내 계정","확인"
    乌克兰语："Я","ОК"
    葡萄牙语："Perfil","Confirmar"
    """
    poco(my).click()
    touch(Template(r"tpl1752817345575.png", record_pos=(0.244, 0.068), resolution=(2048, 2732)))
    touch(Template(r"tpl1752817400705.png", record_pos=(-0.458, -0.548), resolution=(2048, 2732)))
    poco("简体中文").click()
    poco(comfirm).click()
    touch(Template(r"tpl1752816903163.png", record_pos=(-0.459, -0.621), resolution=(2048, 2732)))

if __name__ == "__main__":
    switch_lang_chinese_to_other("Deutsch")
    switch_lang_other_to_chinese("Mein","Bestätigen")# -*- encoding=utf8 -*-
