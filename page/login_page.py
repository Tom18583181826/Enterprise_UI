from common.base import Base
from common.read_elements_file import ReadElementsFile
from common.read_path_file import ReadPathFile


# 登录页面
class LoginPage(Base):
    def __init__(self, browser_type, url):
        super().__init__(browser_type, url)
        self.file_path = ReadPathFile()
        self.elements_path = self.file_path.get_elements_file_path()
        self.elements_data = ReadElementsFile()
        self.elements = self.elements_data.read_elements_data(self.elements_path)

    # 登录流程
    def login(self, username, password, verify_code):
        # 输入用户名
        self.send_keys(self.elements["login"]["login_name"], username)
        # 输入密码
        self.send_keys(self.elements["login"]["password"], password)
        # 输入验证码
        self.send_keys(self.elements["login"]["verify_code"], verify_code)
        # 点击登录按钮
        self.click(self.elements["login"]["submit"])

    # 登陆成功
    def get_login_success(self):
        return self.get_text(self.elements["login"]["login_success"])

    # 用户名为空导致登录失败
    def get_username_null_fail(self):
        return self.get_text(self.elements["login"]["username_null"])

    # 用户名错误导致登录失败
    def get_username_error_fail(self):
        return self.get_text(self.elements["login"]["username_error"])

    # 密码为空导致登录失败
    def get_password_null_fail(self):
        return self.get_text(self.elements["login"]["password_null"])

    # 密码错误导致登录失败
    def get_password_error_fail(self):
        return self.get_text(self.elements["login"]["password_error"])

    # 验证码为空导致登录失败
    def get_verify_null_fail(self):
        return self.get_text(self.elements["login"]["verify_code_null"])


if __name__ == '__main__':
    login_test = LoginPage('Chrome', "http://192.168.0.139:18091/pbf_company/index.html#/login?redirect=%2Fhome")
    login_test.login("12138002", "123456", "111111")
