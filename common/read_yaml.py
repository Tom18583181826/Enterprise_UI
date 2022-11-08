import yaml
from common.read_ini import ReadIni


class ReadYaml:
    def read_yaml_data(self, file_path):
        with open(file_path, encoding="utf8") as file:
            return yaml.safe_load(file)


if __name__ == '__main__':
    read_ini = ReadIni()
    yaml_path = read_ini.get_yaml_file_path()
    read_yaml = ReadYaml()
    yaml_data = read_yaml.read_yaml_data(yaml_path)
    print(yaml_data)
