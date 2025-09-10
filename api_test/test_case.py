import ddt
import unittest
from api_request import *


marketing,FAQ = 0,1
test_marketing_data = case_data.get_excel_data(marketing)
test_FAQ_data = case_data.get_excel_data(FAQ)


@ddt.ddt
class TestRunCaseDdt(unittest.TestCase):

    @ddt.data(*test_marketing_data)
    def test_marketing(self, data):
        run_request(data,marketing)

    @ddt.data(*test_FAQ_data)
    def test_FAQ(self, data):
        run_request(data, FAQ)


