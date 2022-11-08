from common.base import Base
from common.read_ini import ReadIni
from common.read_yaml import ReadYaml


class LoginPage(Base):
    def __init__(self, browser_type, url):
        super().__init__(browser_type, url)
        self.read_ini = ReadIni()
        self.yaml_path = self.read_ini.get_yaml_file_path()
        self.read_yaml = ReadYaml()
        self.yaml_data = self.read_yaml.read_yaml_data(self.yaml_path)

    # 登录流程
    def login(self, username, password, verify_code):
        # 输入用户名
        self.send_keys(self.yaml_data["login"]["login_name"], username)
        # 输入密码
        self.send_keys(self.yaml_data["login"]["password"], password)
        # 输入验证码
        self.send_keys(self.yaml_data["login"]["verify_code"], verify_code)
        # 点击登录按钮
        self.click(self.yaml_data["login"]["submit"])

    # 登陆成功
    def get_login_success(self):
        return self.get_text(self.yaml_data["login"]["login_success"])

    # 用户名为空导致登录失败
    def get_username_null_fail(self):
        return self.get_text(self.yaml_data["login"]["username_null"])

    # 用户名错误导致登录失败
    def get_username_error_fail(self):
        return self.get_text(self.yaml_data["login"]["username_error"])

    # 密码为空导致登录失败
    def get_password_null_fail(self):
        return self.get_text(self.yaml_data["login"]["password_null"])

    # 密码错误导致登录失败
    def get_password_error_fail(self):
        return self.get_text(self.yaml_data["login"]["password_error"])

    # 验证码为空导致登录失败
    def get_verify_null_fail(self):
        return self.get_text(self.yaml_data["login"]["verify_code_null"])


if __name__ == '__main__':
    login_test = LoginPage('Chrome', "http://192.168.0.139:18091/pbf_company/index.html#/login?redirect=%2Fhome")
    login_test.login("12138002", "123456", "111111")
