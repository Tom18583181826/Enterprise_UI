from common.base import Base
from common.read_ini import ReadIni
from common.read_yaml import ReadYaml


class InterestGroupsPage(Base):
    read_ini = ReadIni()
    read_path = read_ini.get_yaml_file_path()
    read_yaml = ReadYaml()
    yaml_data = read_yaml.read_yaml_data(read_path)

    # 点击新建按钮
    def click_create_group(self):
        self.click(self.yaml_data["interest_group"]["create_group"])
