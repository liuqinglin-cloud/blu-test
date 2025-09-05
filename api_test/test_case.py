import ddt
import json
import demjson3
import unittest
from utils.handle_excel import case_data
from utils.handle_ini import environment_ini
from utils.handle_json import header_json
from utils.handle_api_data import get_data
from basic_request import request
from assert_methods import assert_api

current_sheet = 0
test_data = case_data.get_excel_data(current_sheet)
print(test_data)


@ddt.ddt
class TestRunCaseDdt(unittest.TestCase):

    @ddt.data(*test_data)
    def test_case(self, data):
        cookie = None
        header = None
        is_run = data[2]
        case_id = data[0]
        row_num = case_data.get_row_number(case_id)
        if is_run == "yes":
            is_depend = data[3]
            request_data = json.loads(data[9])
            try:
                if is_depend is not None:
                    depend_key = data[4]
                    depend_data = get_data(is_depend)
                    request_data[depend_key] = depend_data
                    request_data = demjson3.encode(request_data)
                method = data[8]
                url = data[7]
                environment = data[5]
                server_name = data[6]
                host = environment_ini.get_value(server_name, environment)
                url = host + url
                except_rule = data[12]
                except_result = data[13]
                cookie_method = data[10]
                is_header = data[11]
                if cookie_method == "yes":
                    pass
                if is_header == "yes":
                    header = header_json.read_json_file()
                res = request(method, url, request_data, cookie, header)
                case_data.excel_write_data(current_sheet, row_num, 16, json.dumps(res, ensure_ascii=False))
                assert_result = assert_api(except_rule,except_result,environment)
                if assert_result is True:
                    case_data.excel_write_data(current_sheet, row_num, 15, "通过")
                else:
                    case_data.excel_write_data(current_sheet, row_num, 15, "失败")
                    raise Exception
            except Exception as e:
                case_data.excel_write_data(current_sheet, row_num, 15, "失败")
                raise e


if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [TestRunCaseDdt('test_case')]
    suite.addTests(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)
