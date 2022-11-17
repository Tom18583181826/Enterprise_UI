from selenium.webdriver import Keys

from common.read_elements_file import ReadYaml
from common.read_path_file import ReadIni
from page.interest_group.interest_group_page import InterestGroupPage


# 成员列表页面
class MemberListPage(InterestGroupPage):
    def __init__(self, browser_type, url):
        super().__init__(browser_type, url)
        self.read_ini = ReadIni()
        self.yaml_path = self.read_ini.get_yaml_file_path()
        self.read_yaml = ReadYaml()
        self.yaml_data = self.read_yaml.read_yaml_data(self.yaml_path)

    # 输入成员名称查询
    def member_name_query(self, member_name):
        self.send_keys(self.yaml_data["member_list"]["member_name"], member_name)
        ele = self.locator_element(self.yaml_data["member_list"]["member_name"])
        ele.send_keys(Keys.ENTER)

    # 输入活动名称查询
    def event_name_query(self, event_name):
        self.send_keys(self.yaml_data["member_list"]["event_name"], event_name)
        ele = self.locator_element(self.yaml_data["member_list"]["event_name"])
        ele.send_keys(Keys.ENTER)

    # 选择小组部门查询
    def team_sector_query(self, sector_type):
        self.click(self.yaml_data["member_list"]["department"])
        if sector_type == 1:
            self.click(self.yaml_data["member_list"]["department_1"])
        elif sector_type == 2:
            self.click(self.yaml_data["member_list"]["department_2"])
        else:
            self.click(self.yaml_data["member_list"]["department_3"])

    # 新增成员
    def add_member(self):
        self.click(self.yaml_data["member_list"]["add_member"])
        self.click(self.yaml_data["member_list"]["select_member"])
        self.click(self.yaml_data["member_list"]["add_member_9527015"])
        self.click(self.yaml_data["member_list"]["submit_member"])

    # 批量删除小组成员
    def batch_delete(self):
        self.click(self.yaml_data["member_list"]["batch_delete"])

    # 点击详情按钮
    def member_details(self):
        self.click(self.yaml_data["member_list"]["member_details"])

    # 点击删除按钮
    def delete_button(self):
        self.click(self.yaml_data["member_list"]["delete_button"])
