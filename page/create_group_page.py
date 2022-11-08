from time import sleep

from common.base import Base
from common.read_ini import ReadIni
from common.read_yaml import ReadYaml


class CreateGroupPage(Base):
    read_ini = ReadIni()
    read_path = read_ini.get_yaml_file_path()
    read_yaml = ReadYaml()
    yaml_data = read_yaml.read_yaml_data(read_path)
    up_file_path = read_ini.get_up_image_path()

    def create_group(self, group_name, up_file_path):
        # 输入小组名称
        self.send_keys(self.yaml_data["create_group"]["group_name"], group_name)
        # 上传小组封面图
        self.up_file(self.yaml_data["create_group"]["cover_image"], up_file_path)


if __name__ == '__main__':
    test = CreateGroupPage("Chrome", "http://192.168.0.139:18091/pbf_company/index.html#/workbench/group")
    sleep(20)
    read_ini = ReadIni()
    up_file_path = read_ini.get_up_image_path()
    test.create_group("123456", up_file_path)
