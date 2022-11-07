import json

from common.read_ini import ReadIni


class ReadJson:
    def read_json_data(self, file_path):
        with open(file_path, encoding="utf8") as file:
            return json.load(file)


if __name__ == '__main__':
    read_ini = ReadIni()
    json_path = read_ini.get_json_file_path()
    read_json = ReadJson()
    json_data = read_json.read_json_data(json_path)
    print(json_data)
