import yaml


# ��ȡҳ��Ԫ���ļ�����ȡ��λҳ��Ԫ�ص����ͺ�ֵ
class ReadElementsFile:
    def read_elements_data(self, file_path):
        with open(file_path, encoding="utf8") as file:
            return yaml.safe_load(file)
