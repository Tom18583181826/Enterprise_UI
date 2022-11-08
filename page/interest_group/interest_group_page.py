# coding=gbk
from time import sleep
from selenium.webdriver import Keys
from common.read_ini import ReadIni
from common.read_yaml import ReadYaml
from page.home_page import HomePage


class InterestGroupPage(HomePage):
    def __init__(self, browser_type, url):
        super().__init__(browser_type, url)
        self.read_ini = ReadIni()
        self.yaml_path = self.read_ini.get_yaml_file_path()
        self.read_yaml = ReadYaml()
        self.yaml_data = self.read_yaml.read_yaml_data(self.yaml_path)

    # 点击新建兴趣小组按钮
    def create_group(self):
        self.click(self.yaml_data["interest_group"]["create_group"])

    # 点击批量删除兴趣小组按钮
    def batch_delete(self):
        self.click(self.yaml_data["interest_group"]["batch_delete"])

    # 输入小组名称查询小组
    def name_query(self, group_name):
        self.send_keys(self.yaml_data["interest_group"]["name_query"], group_name)
        ele = self.locator_element(self.yaml_data["interest_group"]["name_query"])
        ele.send_keys(Keys.ENTER)

    # 点击小组状态查询小组
    def status_query(self, status_type):
        self.click(self.yaml_data["interest_group"]["status_query"])
        if status_type == 1:
            self.click(self.yaml_data["interest_group"]["enable_status"])
        else:
            self.click(self.yaml_data["interest_group"]["disable_status"])


if __name__ == '__main__':
    test = InterestGroupPage('Chrome', "http://192.168.0.139:18091/pbf_company/index.html#/login?redirect=%2Fhome")
    test.login("12138002", "123456", "111111")
    test.status_query(0)
    sleep(10)
    test.quit()
