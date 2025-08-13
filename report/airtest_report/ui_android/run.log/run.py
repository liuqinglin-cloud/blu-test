# -*- encoding=utf8 -*-
__author__ = "admin"


import unittest
import unittestreport
import os.path
import  time
from airtest.report.report import LogToHtml
from test_me import TestMe

case_path = os.path.dirname(__file__)
project_path = os.path.dirname(os.path.dirname(__file__))

testsuite = unittest.TestSuite()
#部分用例，按需添加
tests = [TestMe('test_my_account')]
#所有用例
#tests = unittest.TestLoader().discover(case_path,pattern='test_*.py',top_level_dir=None)
testsuite.addTests(tests)

#unittest报告,按时间命名,不会覆盖
report_path = os.path.join(project_path,"report\\unittest_report\\ui_android")
current_time = time.strftime('%Y%m%d %H%M%S')
file_name = f"report{current_time}.html"
runner = unittestreport.TestRunner(testsuite,
                                   tester='lql',
                                   filename=file_name,
                                   report_dir=report_path,
                                   title="UI测试报告",
                                   desc="android UI测试",
                                   templates=3
                                   )

#执行
try:
    runner.run()

#导出airtest报告，方便看翻译测试截图，runner执行后会停止，finally保证生成airtest报告，报告会覆盖
finally:
    common_android_path = os.path.join(project_path,"common_android")
    script_path = os.path.join(case_path,"run.py")
    log_path = os.path.join(common_android_path,"log")
    logfile_path = os.path.join(common_android_path,"log\\log.txt")
    export_path = os.path.join(project_path,"report\\airtest_report\\ui_android")
    h1 = LogToHtml(script_root=script_path,
                   log_root=log_path,
                   export_dir=export_path,
                   logfile=logfile_path,
                   lang='zh',
                   plugins=["poco.utils.airtest.report"])
    h1.report()