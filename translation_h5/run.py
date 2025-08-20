__author__ = "刘青林"

import unittest
import unittestreport
import os.path
import time
from airtest.report.report import LogToHtml



case_path = os.path.dirname(__file__)
project_path = os.path.dirname(os.path.dirname(__file__))

testsuite = unittest.TestSuite()
#部分用例，按需添加
#tests = [TestSimplifiedChinese('test_me'),TestEnglish("test_me")]
#匹配用例文件
tests = unittest.TestLoader().discover(case_path,pattern='translation_*.py',top_level_dir=None)
testsuite.addTests(tests)
runner=unittest.TextTestRunner()


#执行
try:
    runner.run(testsuite)

#使用Android手机测试，导出airtest报告，方便看翻译测试截图，runner执行后会停止，finally保证生成airtest报告，报告会覆盖
finally:
    common_android_path = os.path.join(project_path,"common_android")
    script_path = os.path.join(case_path,"run.py")
    log_path = os.path.join(common_android_path,"log")
    logfile_path = os.path.join(common_android_path,"log\\log.txt")
    export_path = os.path.join(project_path,"report\\airtest_report\\translation_h5")
    h1 = LogToHtml(script_root=script_path,
                   log_root=log_path,
                   export_dir=export_path,
                   logfile=logfile_path,
                   lang='zh',
                   plugins=["poco.utils.airtest.report"])
    h1.report()
