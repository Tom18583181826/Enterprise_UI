from openpyxl import load_workbook
from common.read_ini import ReadIni
from common.read_json import ReadJson
from data.excel_column import ExcelColumn


class ReadExcel:
    def __init__(self):
        self.read_ini = ReadIni()
        self.excel_path = self.read_ini.get_excel_file_path()
        self.params_file_path = self.read_ini.get_json_file_path()
        self.expect_file_path = self.read_ini.get_json_file_path()
        self.wb = load_workbook(self.excel_path)
        self.wb_sheet = self.wb[self.read_ini.get_sheet_name()]

    def get_cell_value(self, column, row):
        return self.wb_sheet[column + str(row)].value

    def get_case_id(self, row):
        return self.get_cell_value(ExcelColumn.CASE_ID, row)

    def get_case_name(self, row):
        return self.get_cell_value(ExcelColumn.CASE_NAME, row)

    def get_case_params_key(self, row):
        return self.get_cell_value(ExcelColumn.CASE_PARAMS_KEY, row)

    def get_case_params_value(self, row):
        if self.get_case_params_key(row):
            return ReadJson().read_json_data(self.params_file_path)[self.get_case_params_key(row)]

    def get_case_expect_key(self, row):
        return self.get_cell_value(ExcelColumn.CASE_EXPECT_KEY, row)

    def get_case_expect_value(self, row):
        if self.get_case_expect_key(row):
            return ReadJson().read_json_data(self.expect_file_path)[self.get_case_expect_key(row)]

    def get_row_count(self):
        return self.wb_sheet.max_row


if __name__ == '__main__':
    read = ReadExcel()
    data_list = []
    for row in range(2, read.get_row_count() + 1):
        id = read.get_case_id(row)
        name = read.get_case_name(row)
        params = read.get_case_params_value(row)
        expect = read.get_case_expect_value(row)
        data_list.append((id, name, params, expect))
    print(data_list)
