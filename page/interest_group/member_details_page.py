from selenium.webdriver import Keys

from common.read_elements_file import ReadYaml
from common.read_path_file import ReadIni
from page.interest_group.member_list_page import MemberListPage


# ��Ա����ҳ��
class MenberDetailsPage(MemberListPage):
    def __init__(self, browser_type, url):
        super().__init__(browser_type, url)
        self.read_ini = ReadIni()
        self.yaml_path = self.read_ini.get_yaml_file_path()
        self.read_yaml = ReadYaml()
        self.yaml_data = self.read_yaml.read_yaml_data(self.yaml_path)

    # ѡ���������Ͳ�ѯ
    def post_type_query(self, post_type):
        self.click(self.yaml_data["member_details"]["post_type"])
        if post_type == 1:
            self.click(self.yaml_data["member_details"]["text_type"])
        elif post_type == 2:
            self.click(self.yaml_data["member_details"]["image_type"])
        else:
            self.click(self.yaml_data["member_details"]["text_and_image"])

    # ����ʱ���ѯ
    def publish_time_query(self, start_time, stop_time):
        self.send_keys(self.yaml_data["member_details"]["start_time"], start_time)
        self.send_keys(self.yaml_data["member_details"]["stop_time"], stop_time)
        ele = self.locator_element(self.yaml_data["member_details"]["stop_time"])
        ele.send_keys(Keys.ENTER)

    # ����˳���ѯ
    def publication_order_query(self, order_type):
        self.click(self.yaml_data["member_details"]["publication_order"])
        if order_type == 1:
            self.click(self.yaml_data["member_details"]["order_type"])
        else:
            self.click(self.yaml_data["member_details"]["reverse_type"])

    # ��ѯ��ɾ������
    def delete_post_query(self):
        self.click(self.yaml_data["member_details"]["delete_post_query"])

    # ����ɾ����ť
    def batch_delete(self):
        self.click(self.yaml_data["member_details"]["batch_delete"])

    # �鿴��������
    def view_details(self):
        self.click(self.yaml_data["member_details"]["view_details"])

    # �ö�/ȡ���ö�
    def sticky(self):
        self.click(self.yaml_data["member_details"]["sticky"])

    # ɾ����ť
    def delete_button(self):
        self.click(self.yaml_data["member_details"]["delete_button"])

    # �����Ѳ���ҳ��
    def participated_activities(self):
        self.click(self.yaml_data["member_details"]["participated_activities"])

    # ����Ͳ�ѯ
    def event_type_query(self, event_type):
        self.click(self.yaml_data["member_details"]["event_type"])
