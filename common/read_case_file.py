import json

from openpyxl import load_workbook

from common.get_json_value_by_key import GetJsonValue
from common.read_path_file import ReadPathFile
from data.excel_column import ExcelColumn


# 读取测试用例表格，获取测试用例
class ReadCaseFile:
    def __init__(self):
        self.read_ini = ReadPathFile()
        self.case_path = self.read_ini.get_case_file_path()
        self.params_file_path = self.read_ini.get_data_file_path()
        self.expect_file_path = self.read_ini.get_data_file_path()
        self.wb = load_workbook(self.case_path)
        self.wb_sheet = self.wb[self.read_ini.get_sheet_name()]

    # 获取单元格内容
    def get_cell_value(self, column, row):
        return self.wb_sheet[column + str(row)].value

    # 获取用例ID
    def get_case_id(self, row):
        return self.get_cell_value(ExcelColumn.CASE_ID, row)

    # 获取用例名称
    def get_case_name(self, row):
        return self.get_cell_value(ExcelColumn.CASE_NAME, row)

    # 获取参数的key
    def get_case_params_key(self, row):
        return self.get_cell_value(ExcelColumn.CASE_PARAMS_KEY, row)

    # 获取参数的value
    def get_case_params_value(self, row):
        if self.get_case_params_key(row):
            read_ini = ReadIni()
            json_path = read_ini.get_json_file_path()
            with open(json_path, encoding="utf8") as file:
                result = GetJsonValue().get_json_value_by_key(json.load(file), self.get_case_params_key(row))
                return result

    # 获取预期结果的key
    def get_case_expect_key(self, row):
        return self.get_cell_value(ExcelColumn.CASE_EXPECT_KEY, row)

    # 获取预期结果的value
    def get_case_expect_value(self, row):
        if self.get_case_expect_key(row):
            read_ini = ReadIni()
            json_path = read_ini.get_json_file_path()
            with open(json_path, encoding="utf8") as file:
                result = GetJsonValue().get_json_value_by_key(json.load(file), self.get_case_expect_key(row))
                return result
