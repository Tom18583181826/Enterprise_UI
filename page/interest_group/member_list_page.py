from selenium.webdriver import Keys

from common.read_elements_file import ReadYaml
from common.read_path_file import ReadIni
from page.interest_group.interest_group_page import InterestGroupPage


# ��Ա�б�ҳ��
class MemberListPage(InterestGroupPage):
    def __init__(self, browser_type, url):
        super().__init__(browser_type, url)
        self.read_ini = ReadIni()
        self.yaml_path = self.read_ini.get_yaml_file_path()
        self.read_yaml = ReadYaml()
        self.yaml_data = self.read_yaml.read_yaml_data(self.yaml_path)

    # �����Ա���Ʋ�ѯ
    def member_name_query(self, member_name):
        self.send_keys(self.yaml_data["member_list"]["member_name"], member_name)
        ele = self.locator_element(self.yaml_data["member_list"]["member_name"])
        ele.send_keys(Keys.ENTER)

    # �������Ʋ�ѯ
    def event_name_query(self, event_name):
        self.send_keys(self.yaml_data["member_list"]["event_name"], event_name)
        ele = self.locator_element(self.yaml_data["member_list"]["event_name"])
        ele.send_keys(Keys.ENTER)

    # ѡ��С�鲿�Ų�ѯ
    def team_sector_query(self, sector_type):
        self.click(self.yaml_data["member_list"]["department"])
        if sector_type == 1:
            self.click(self.yaml_data["member_list"]["department_1"])
        elif sector_type == 2:
            self.click(self.yaml_data["member_list"]["department_2"])
        else:
            self.click(self.yaml_data["member_list"]["department_3"])

    # ������Ա
    def add_member(self):
        self.click(self.yaml_data["member_list"]["add_member"])
        self.click(self.yaml_data["member_list"]["select_member"])
        self.click(self.yaml_data["member_list"]["add_member_9527015"])
        self.click(self.yaml_data["member_list"]["submit_member"])

    # ����ɾ��С���Ա
    def batch_delete(self):
        self.click(self.yaml_data["member_list"]["batch_delete"])

    # ������鰴ť
    def member_details(self):
        self.click(self.yaml_data["member_list"]["member_details"])

    # ���ɾ����ť
    def delete_button(self):
        self.click(self.yaml_data["member_list"]["delete_button"])
