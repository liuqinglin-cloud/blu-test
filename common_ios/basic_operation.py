# -*- encoding=utf8 -*-
__author__ = "admin"
import os.path
import sys
project_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_path)
from utils.handle_ini import local_element_ios_ini
from airtest.core.api import *
from airtest.cli.parser import cli_setup
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/1C231FDF60050J?cap_method=ADBCAP&touch_method=MAXTOUCH&",])

from poco.drivers.ios import iosPoco
poco = iosPoco()




def find_ele(section, key):
    value_list = local_element_ios_ini(section, key)
    text = value_list[0]
    name_ios = value_list[2]
    try:
        ele = poco(name_ios)
        return ele
    except:
        ele = poco(name=name_ios, text=text)
        return ele

def click_ele(section, key):
    find_ele(section, key).click()


