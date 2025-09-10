import unittest
import unittestreport
import time
import os.path
from test_case import TestRunCaseDdt


case_path = os.path.dirname(__file__)
project_path = os.path.dirname(os.path.dirname(__file__))

testsuite = unittest.TestSuite()
#tests = [TestRunCaseDdt('test_marketing')]
tests = unittest.TestLoader().discover(case_path,pattern='test_*.py',top_level_dir=None)
testsuite.addTests(tests)
report_path = os.path.join(project_path, "report\\unittest_report\\api_test")
#current_time = time.strftime('%Y%m%d %H%M%S')
#file_name = f"report{current_time}.html"
file_name = "report.html"
runner = unittestreport.TestRunner(testsuite,
                                   tester='lql',
                                   filename=file_name,
                                   report_dir=report_path,
                                   title="接口测试报告",
                                   desc="接口测试",
                                   templates=1
                                   )
runner.run()