# -*- encoding=utf8 -*-
__author__ = "admin"


import unittest
import os.path
import sys
project_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_path)
from common_android.assert_methods import assert_ele_is_exist
from common_android.app_operation import *

class TestMe(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_address(self):
        pass
