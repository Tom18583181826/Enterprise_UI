import time

import pytest

from common.get_json_value_by_key import GetJsonValue
from common.get_log import GetLog
from common.read_case_file import ReadCaseFile
from common.read_path_file import ReadPathFile
from page.login_page import LoginPage


# 获取登录成功用例的数据
def get_success_data():
    read = ReadCaseFile()
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
    read = ReadCaseFile()
    failed_list = []
    for row in range(3, 8):
        case_id = read.get_case_id(row)
        case_name = read.get_case_name(row)
        params = read.get_case_params_value(row)
        expect = read.get_case_expect_value(row)
        failed_list.append((case_id, case_name, params, expect))
    return failed_list


# 测试登录
class TestLogin:
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")

    def setup(self):
        self.login_test = LoginPage("Chrome",
                                    "http://192.168.0.139:18091/pbf_company/index.html#/login?redirect=%2Fhome")

    def teardown(self):
        self.login_test.quit()

    # 测试登录成功的用例
    @pytest.mark.parametrize("case_id,case_name,params,expect", get_success_data())
    def test_login_success(self, case_id, case_name, params, expect):
        try:
            username = GetJsonValue().get_json_value_by_key(params, "username")
            password = GetJsonValue().get_json_value_by_key(params, "password")
            verify_code = GetJsonValue().get_json_value_by_key(params, "verify_code")
            self.login_test.login(username, password, verify_code)
            success_text = self.login_test.get_login_success()
            assert expect[0] == success_text
        except AssertionError:
            self.login_test.get_screenshot(
                ReadPathFile().get_screenshot_file_path() + "screenshot_{}.png".format(self.now_time))
            log_obj = GetLog().get_log(ReadPathFile().get_log_file_path() + "login{}.log".format(self.now_time))
            log_obj.error("用例{}---{}---执行失败！".format(case_id, case_name))
            raise AssertionError("用例{}---{}---执行失败！".format(case_id, case_name))
        finally:
            pass

    # 测试登陆失败的用例
    @pytest.mark.parametrize("case_id, case_name, params, expect", get_failed_data())
    def test_login_fail(self, case_id, case_name, params, expect):
        try:
            username = GetJsonValue().get_json_value_by_key(params, "username")
            password = GetJsonValue().get_json_value_by_key(params, "password")
            verify_code = GetJsonValue().get_json_value_by_key(params, "verify_code")
            self.login_test.login(username, password, verify_code)
            if expect == "用户名不存在":
                fail_text = self.login_test.get_username_error_fail()
                assert expect[0] == fail_text
            if expect == "请输入账号":
                fail_text = self.login_test.get_username_null_fail()
                assert expect[0] == fail_text
            if expect == "密码不正确":
                fail_text = self.login_test.get_password_error_fail()
                assert expect[0] == fail_text
            if expect == "请输入登录密码":
                fail_text = self.login_test.get_password_null_fail()
                assert expect[0] == fail_text
            if expect == "请输入验证码":
                fail_text = self.login_test.get_verify_null_fail()
                assert expect[0] == fail_text
        except AssertionError:
            self.login_test.get_screenshot(
                ReadPathFile().get_screenshot_file_path() + "screenshot_{}.png".format(self.now_time))
            log_obj = GetLog().get_log(ReadPathFile().get_log_file_path() + "login{}.log".format(self.now_time))
            log_obj.error("用例{}---{}---执行失败！".format(case_id, case_name))
            raise AssertionError("用例{}---{}---执行失败！".format(case_id, case_name))
        finally:
            pass


if __name__ == '__main__':
    pytest.main()
