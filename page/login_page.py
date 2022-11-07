from time import sleep
from common.base import Base
from common.read_ini import ReadIni
from common.read_yaml import ReadYaml


class LoginPage(Base):
    read_ini = ReadIni()
    read_path = read_ini.get_yaml_file_path()
    read_yaml = ReadYaml()
    yaml_data = read_yaml.read_yaml_data(read_path)

    def login(self, username, password, verify_code):
        # 输入用户名
        self.send_keys(self.yaml_data["login"]["login_name"], username)
        # 输入密码
        self.send_keys(self.yaml_data["login"]["password"], password)
        # 输入验证码
        self.send_keys(self.yaml_data["login"]["verify_code"], verify_code)
        # 点击登录按钮
        self.click(self.yaml_data["login"]["submit"])
        sleep(10)

    def get_login_success(self):
        success_text = self.get_text(self.yaml_data["login"]["login_success"])
        return success_text

    # 用户名为空导致登录失败
    def get_name_null_fail(self):
        return self.get_text(self.yaml_data["login"]["username_null"])

    # 密码为空导致登录失败
    def get_password_null_fail(self):
        return self.get_text(self.yaml_data["login"]["password_null"])

    # 验证码为空导致登录失败
    def get_verify_null_fail(self):
        return self.get_text(self.yaml_data["login"]["verify_code_null"])


if __name__ == '__main__':
    login_test = LoginPage('Chrome', "http://192.168.0.139:18091/pbf_company/index.html#/login?redirect=%2Fhome")
    login_test.login("12138001", "123456", "111111")
