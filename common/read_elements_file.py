import yaml


# 读取页面元素文件，获取定位页面元素的类型和值
class ReadElementsFile:
    def read_elements_data(self, file_path):
        with open(file_path, encoding="utf8") as file:
            return yaml.safe_load(file)
