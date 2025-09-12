import ddt
import unittest
from api_request import run_request
from utils.handle_excel import case_data

marketing,FAQ = 0,1
test_blu_marketing_center_data = case_data.get_excel_data(marketing)
test_FAQ_data = case_data.get_excel_data(FAQ)


@ddt.ddt
class TestCase(unittest.TestCase):

    @ddt.data(*test_blu_marketing_center_data)
    def test_blu_marketing_center(self, data):
        run_request(data,marketing)

    @ddt.data(*test_FAQ_data)
    def test_FAQ(self, data):
        run_request(data, FAQ)


