__author__ = "刘青林"

import unittest
import unittestreport
import os.path
import time
from airtest.report.report import LogToHtml
from translation_simplified_chinese import TestSimplifiedChinese
from translation_english import TestEnglish


case_path = os.path.dirname(__file__)
project_path = os.path.dirname(os.path.dirname(__file__))

testsuite = unittest.TestSuite()
#部分用例，按需添加
#tests = [TestSimplifiedChinese('test_me'),TestEnglish("test_me")]
#匹配用例文件
tests = unittest.TestLoader().discover(case_path,pattern='translation_si*.py',top_level_dir=None)
testsuite.addTests(tests)


report_path = os.path.join(project_path,"report\\unittest_report\\translation_android")
#current_time = time.strftime('%Y%m%d %H%M%S')
#file_name = f"report{current_time}.html"
file_name = "report.html"
runner = unittestreport.TestRunner(testsuite,
                                   tester='lql',
                                   filename=file_name,
                                   report_dir=report_path,
                                   title="翻译测试报告",
                                   desc="android翻译测试",
                                   templates=1
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
    export_path = os.path.join(project_path,"report\\airtest_report\\translation_android")
    h1 = LogToHtml(script_root=script_path,
                   log_root=log_path,
                   export_dir=export_path,
                   logfile=logfile_path,
                   lang='zh',
                   plugins=["poco.utils.airtest.report"])
    h1.report()











