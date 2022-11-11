import time

import pytest

from common.get_json_value_by_key import GetJsonValue
from common.get_log import GetLog
from common.read_excel import ReadExcel
from common.read_ini import ReadIni
from common.read_yaml import ReadYaml
from page.interest_group.create_interest_group_page import CreateIntGroPage


# 获取创建兴趣小组成功的数据
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


class TestCreateIntGro(CreateIntGroPage):
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")

    read_ini = ReadIni()
    yaml_path = read_ini.get_yaml_file_path()
    read_yaml = ReadYaml()
    yaml_data = read_yaml.read_yaml_data(yaml_path)

    def setup(self):
        self.create_test = CreateIntGroPage("Chrome",
                                            "http://192.168.0.139:18091/pbf_company/index.html#/login?redirect=%2Fhome")

    def teardown(self):
        self.create_test.quit()

    # 测试创建兴趣小组成功的用例
    @pytest.mark.parametrize("case_id, case_name, params, expect", get_create_success_data())
    def test_create_success(self, case_id, case_name, params, expect):
        try:
            ele = self.locator_element(self.yaml_data["home"]["interest_groups"])
            js = "arguments[0].scrollIntoView()"
            self.wd.execute_script(js, ele)
            self.click(self.yaml_data["home"]["interest_groups"])
            self.create_test.create_group()
            group_name = GetJsonValue().get_json_value_by_key(params, "group_name")
            group_introduction = GetJsonValue().get_json_value_by_key(params, "group_introduction")
            scope_type = GetJsonValue().get_json_value_by_key(params, "scope_type")
            self.create_test.create_int_group(group_name, group_introduction, scope_type)
            success_text = self.create_test.create_group_success()
            assert expect[0] == success_text
        except AssertionError:
            self.create_test.get_screenshot(
                ReadIni().get_screenshot_file_path() + "screenshot_{}.png".format(self.now_time))
            log_obj = GetLog().get_log(ReadIni().get_log_file_path() + "login{}.log".format(self.now_time))
            log_obj.error("用例{}---{}---执行失败！".format(case_id, case_name))
            raise AssertionError("用例{}---{}---执行失败！".format(case_id, case_name))
        finally:
            pass


if __name__ == '__main__':
    pytest.main()
