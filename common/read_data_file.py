import json


# 读取测试数据文件，获取测试数据和预期结果的数据
class ReadDataFile:
    def read_test_data(self, file_path):
        with open(file_path, encoding="utf8") as file:
            return json.load(file)
