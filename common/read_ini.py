import os
from configparser import ConfigParser


# 读取Ini文件，获取文件路径
class ReadIni:
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
    def get_excel_file_path(self):
        return os.path.join(self.base_path, self.config.get("Path", "excel_path"))

    # 获取Sheet页名称
    def get_sheet_name(self):
        return self.config.get("Path", "sheet_name")

    # 获取Json文件路径
    def get_json_file_path(self):
        return os.path.join(self.base_path, self.config.get("Path", "json_path"))

    # 获取Yaml文件路径
    def get_yaml_file_path(self):
        return os.path.join(self.base_path, self.config.get("Path", "yaml_path"))


if __name__ == '__main__':
    read = ReadIni()
    print(read.get_log_file_path())
    print(read.get_report_file_path())
    print(read.get_screenshot_file_path())
    print(read.get_excel_file_path())
    print(read.get_sheet_name())
    print(read.get_json_file_path())
    print(read.get_yaml_file_path())
