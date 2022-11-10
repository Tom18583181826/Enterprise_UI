import time
import pytest

from common.base import Base
from common.read_excel import ReadExcel
from page.login_page import LoginPage


def get_create_success_data():
    read = ReadExcel()
    success_list = []
    for row in range(8, 9):
        case_id = read.get_case_id(row)
        case_name = read.get_case_name(row)
        params = read.get_case_params_value(row)
        expect = read.get_case_expect_value(row)
        success_list.append((case_id, case_name, params, expect))
    return success_list


class TestCreateIntGro:
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")

    def setup(self):
        self.create_test = LoginPage("Chrome",
                                     "http://192.168.0.139:18091/pbf_company/index.html#/login?redirect=%2Fhome")

    def teardown(self):
        self.create_test.quit()

    # 测试创建兴趣小组成功的用例
    @pytest.mark.parametrize("case_id, case_name, params, expect", get_create_success_data())
    def test_create_success(self, case_id, case_name, params, expect):
            pass
