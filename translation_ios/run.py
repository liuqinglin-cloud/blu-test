__author__ = "刘青林"

import unittest
import unittestreport
import os.path
import time
from airtest.report.report import LogToHtml



case_path = os.path.dirname(__file__)
project_path = os.path.dirname(os.path.dirname(__file__))

testsuite = unittest.TestSuite()
#tests = [TestSimplifiedChinese('test_me'),TestEnglish("test_me")]
tests = unittest.TestLoader().discover(case_path,pattern='translation_*.py',top_level_dir=None)
testsuite.addTests(tests)


report_path = os.path.join(project_path,"report\\unittest_report\\translation_ios")
#current_time = time.strftime('%Y%m%d %H%M%S')
#file_name = f"report{current_time}.html"
file_name = "report.html"
runner = unittestreport.TestRunner(testsuite,
                                   tester='lql',
                                   filename=file_name,
                                   report_dir=report_path,
                                   title="翻译测试报告",
                                   desc="ios翻译测试",
                                   templates=1
                                   )
try:
    runner.run()
finally:
    common_ios_path = os.path.join(project_path,"common_ios")
    script_path = os.path.join(case_path,"run.py")
    log_path = os.path.join(common_ios_path,"log")
    logfile_path = os.path.join(common_ios_path,"log\\log.txt")
    export_path = os.path.join(project_path,"report\\airtest_report\\translation_ios")
    h1 = LogToHtml(script_root=script_path,
                   log_root=log_path,
                   export_dir=export_path,
                   logfile=logfile_path,
                   lang='zh',
                   plugins=["poco.utils.airtest.report"])
    h1.report()