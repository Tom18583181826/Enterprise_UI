import json


# ��ȡ���������ļ�����ȡ�������ݺ�Ԥ�ڽ��������
class ReadDataFile:
    def read_test_data(self, file_path):
        with open(file_path, encoding="utf8") as file:
            return json.load(file)
