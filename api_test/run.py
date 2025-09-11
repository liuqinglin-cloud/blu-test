import unittest
import os.path
from test_case import TestCase


case_path = os.path.dirname(__file__)
project_path = os.path.dirname(os.path.dirname(__file__))

testsuite = unittest.TestSuite()
#tests = [TestCase('test_marketing')]
tests = unittest.TestLoader().discover(case_path,pattern='test_*.py',top_level_dir=None)
testsuite.addTests(tests)
testsuite.addTests(tests)
runner=unittest.TextTestRunner()
runner.run(testsuite)