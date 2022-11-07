import time
import pytest
from common.get_log import GetLog
from common.read_excel import ReadExcel
from common.read_ini import ReadIni
from page.login_page import LoginPage


# 获取登录成功用例的数据
def get_success_data():
    read = ReadExcel()
    success_list = []
    for row in range(2, 3):
        case_id = read.get_case_id(row)
        case_name = read.get_case_name(row)
        params = read.get_case_params_value(row)
        expect = read.get_case_expect_value(row)
        success_list.append((case_id, case_name, params, expect))
    return success_list


# 获取登录失败用例的数据
def get_failed_data():
    read = ReadExcel()
    failed_list = []
    for row in range(3, read.get_row_count() + 1):
        case_id = read.get_case_id(row)
        case_name = read.get_case_name(row)
        params = read.get_case_params_value(row)
        expect = read.get_case_expect_value(row)
        failed_list.append((case_id, case_name, params, expect))
    return failed_list


class TestLogin:
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")

    def setUp(self):
        self.login_test = LoginPage("Chrome",
                                    "http://192.168.0.139:18091/pbf_company/index.html#/login?redirect=%2Fhome")

    def tearDown(self):
        self.login_test.quit()

    # 测试登录成功的用例
    @pytest.mark.parametrize("case_id,case_name,params,expect", get_success_data())
    def test_login_success(self, case_id, case_name, params, expect):
        try:
            username = params["username"]
            password = params["password"]
            verify_code = params["verify_code"]
            self.login_test.login(username, password, verify_code)
            success_text = self.login_test.get_login_success()
            if expect != success_text:
                raise AssertionError
        except AssertionError:
            # 用例执行失败执行截图操作
            self.login_test.get_screenshot(
                ReadIni().get_screenshot_file_path() + "screenshot_{}.png".format(self.now_time))
            # 实例化打印日志对象
            log_obj = GetLog().get_log(ReadIni().get_log_file_path() + "login{}.log".format(self.now_time))
            # 打印日志
            log_obj.error("用例{}---{}---执行失败！".format(case_id, case_name))
            raise AssertionError("用例{}---{}---执行失败！".format(case_id, case_name))
        finally:
            pass

    # 测试登陆失败的用例
    @pytest.mark.parametrize("case_id, case_name, params, expect", get_failed_data())
    def test_login_fail(self, case_id, case_name, params, expect):
        try:
            username = params["username"]
            password = params["password"]
            verify_code = params["verify_code"]
            self.login_test.login(username, password, verify_code)
            fail_text = self.login_test.get_namenull_fail()
            if expect != fail_text:
                raise AssertionError
        except AssertionError:
            # 用例执行失败执行截图操作
            self.login_test.get_screenshot(
                ReadIni().get_screenshot_file_path() + "screenshot_{}.png".format(self.now_time))
            # 实例化打印日志对象
            log_obj = GetLog().get_log(ReadIni().get_log_file_path() + "login{}.log".format(self.now_time))
            # 打印日志
            log_obj.error("用例{}---{}---执行失败！".format(case_id, case_name))
            # 使用raise抛出一个指定异常
            raise AssertionError("用例{}---{}---执行失败！".format(case_id, case_name))
        finally:
            pass


if __name__ == '__main__':
    pytest.main()
