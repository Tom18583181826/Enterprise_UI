from selenium.webdriver import Keys

from common.read_elements_file import ReadElementsFile
from common.read_path_file import ReadPathFile
from page.interest_group.interest_group_page import InterestGroupPage


# ��Ա�б�ҳ��
class MemberListPage(InterestGroupPage):
    def __init__(self, browser_type, url):
        super().__init__(browser_type, url)
        self.file_path = ReadPathFile()
        self.elements_path = self.file_path.get_elements_file_path()
        self.elements_data = ReadElementsFile()
        self.elements = self.elements_data.read_elements_data(self.elements_path)

    # �����Ա���Ʋ�ѯ
    def member_name_query(self, member_name):
        self.send_keys(self.elements["member_list"]["member_name"], member_name)
        ele = self.locator_element(self.elements["member_list"]["member_name"])
        ele.send_keys(Keys.ENTER)

    # �������Ʋ�ѯ
    def event_name_query(self, event_name):
        self.send_keys(self.elements["member_list"]["event_name"], event_name)
        ele = self.locator_element(self.elements["member_list"]["event_name"])
        ele.send_keys(Keys.ENTER)

    # ѡ��С�鲿�Ų�ѯ
    def team_sector_query(self, sector_type):
        self.click(self.elements["member_list"]["department"])
        if sector_type == 1:
            self.click(self.elements["member_list"]["department_1"])
        elif sector_type == 2:
            self.click(self.elements["member_list"]["department_2"])
        else:
            self.click(self.elements["member_list"]["department_3"])

    # ������Ա
    def add_member(self):
        self.click(self.elements["member_list"]["add_member"])
        self.click(self.elements["member_list"]["select_member"])
        self.click(self.elements["member_list"]["add_member_9527015"])
        self.click(self.elements["member_list"]["submit_member"])

    # ����ɾ��С���Ա
    def batch_delete(self):
        self.click(self.elements["member_list"]["batch_delete"])

    # ������鰴ť
    def member_details(self):
        self.click(self.elements["member_list"]["member_details"])

    # ���ɾ����ť
    def delete_button(self):
        self.click(self.elements["member_list"]["delete_button"])
