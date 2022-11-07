import os
from configparser import ConfigParser


class ReadIni:
    def __init__(self):
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.config = ConfigParser()
        ini_file_path = os.path.join(self.base_path, r"data\read_ini.ini")
        self.config.read(ini_file_path, encoding="utf-8")

    def get_log_file_path(self):
        return os.path.join(self.base_path, self.config.get("Path", "log_path"))
        # get(section,option):获取section(节)中option的值。返回为string类型

    def get_report_file_path(self):
        return os.path.join(self.base_path, self.config.get("Path", "report_path"))

    def get_screenshot_file_path(self):
        return os.path.join(self.base_path, self.config.get("Path", "screenshot_path"))

    def get_excel_file_path(self):
        return os.path.join(self.base_path, self.config.get("Path", "excel_path"))

    def get_sheet_name(self):
        return self.config.get("Path", "sheet_name")

    def get_json_file_path(self):
        return os.path.join(self.base_path, self.config.get("Path", "json_path"))

    def get_yaml_file_path(self):
        return os.path.join(self.base_path, self.config.get("Path", "yaml_path"))


if __name__ == '__main__':
    read = ReadIni()
    print(read.get_log_file_path())
    print(read.get_report_file_path())
    print(read.get_screenshot_file_path())
    print(read.get_excel_file_path())
    print(read.get_json_file_path())
    print(read.get_yaml_file_path())
    print(read.get_sheet_name())
