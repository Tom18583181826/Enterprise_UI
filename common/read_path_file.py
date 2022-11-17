import os
from configparser import ConfigParser


# 读取配置文件，获取文件路径
class ReadPathFile:
    def __init__(self):
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.config = ConfigParser()
        ini_file_path = os.path.join(self.base_path, r"data\path.ini")
        self.config.read(ini_file_path, encoding="utf-8")

    # 获取日志文件路径
    def get_log_file_path(self):
        return os.path.join(self.base_path, self.config.get("Path", "log_path"))

    # 获取测试报告文件路径
    def get_report_file_path(self):
        return os.path.join(self.base_path, self.config.get("Path", "report_path"))

    # 获取截图文件路径
    def get_screenshot_file_path(self):
        return os.path.join(self.base_path, self.config.get("Path", "screenshot_path"))

    # 获取用例表格文件路径
    def get_case_file_path(self):
        return os.path.join(self.base_path, self.config.get("Path", "case_path"))

    # 获取用例所在Sheet页名称
    def get_sheet_name(self):
        return self.config.get("Path", "sheet_name")

    # 获取测试数据文件路径
    def get_data_file_path(self):
        return os.path.join(self.base_path, self.config.get("Path", "data_path"))

    # 获取页面元素文件路径
    def get_elements_file_path(self):
        return os.path.join(self.base_path, self.config.get("Path", "elements_path"))
