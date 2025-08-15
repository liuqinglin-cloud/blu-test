__author__ = "刘青林"

import unittest
import os.path


case_path = os.path.dirname(__file__)


testsuite = unittest.TestSuite()
discover = unittest.TestLoader().discover(case_path,pattern='test_*.py',top_level_dir=None)
testsuite.addTest(discover)
runner=unittest.TextTestRunner()
runner.run(testsuite)


