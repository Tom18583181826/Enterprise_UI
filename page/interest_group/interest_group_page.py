# coding=gbk
from time import sleep

from selenium.webdriver import Keys

from common.read_elements_file import ReadYaml
from common.read_path_file import ReadIni
from page.home_page import HomePage


# 兴趣小组页面
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

    # 点击编辑小组按钮
    def update_group(self):
        self.click(self.yaml_data["interest_group"]["update_group"])

    # 点击查看成员按钮
    def view_members(self):
        self.click(self.yaml_data["interest_group"]["view_members"])

    # 点击查看帖子按钮
    def view_post(self):
        self.click(self.yaml_data["interest_group"]["view_post"])

    # 点击查看活动按钮
    def view_events(self):
        self.click(self.yaml_data["interest_group"]["view_events"])

    # 点击启用/停用按钮
    def status_button(self):
        self.click(self.yaml_data["interest_group"]["status_button"])

    # 点击删除按钮
    def delete_button(self):
        self.click(self.yaml_data["interest_group"]["delete_button"])


if __name__ == '__main__':
    test = InterestGroupPage('Chrome', "http://192.168.0.139:18091/pbf_company/index.html#/login?redirect=%2Fhome")
    test.login("12138002", "123456", "111111")
    test.status_query(0)
    sleep(10)
    test.quit()
