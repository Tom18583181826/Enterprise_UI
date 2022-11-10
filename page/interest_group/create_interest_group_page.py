# coding=gbk
from common.read_ini import ReadIni
from common.read_yaml import ReadYaml
from page.interest_group.interest_group_page import InterestGroupPage


class CreateIntGroPage(InterestGroupPage):
    def __init__(self, browser_type, url):
        super().__init__(browser_type, url)
        self.read_ini = ReadIni()
        self.yaml_path = self.read_ini.get_yaml_file_path()
        self.read_yaml = ReadYaml()
        self.yaml_data = self.read_yaml.read_yaml_data(self.yaml_path)

    # �½���ȤС��
    def create_int_group(self, group_name, group_introduction, scope_type):
        # ����С������
        self.send_keys(self.yaml_data["create_interest_group"]["group_name"], group_name)
        # �ϴ�С�����ͼ
        # ����С�����
        self.send_keys(self.yaml_data["create_interest_group"]["group_introduction"], group_introduction)
        # ѡ��ɼ���Χ
        if scope_type == 1:
            self.click(self.yaml_data["create_interest_group"]["all_departments"])
            # ��ӹ���Ա
            self.click(self.yaml_data["create_interest_group"]["admins"])
            self.click(self.yaml_data["create_interest_group"]["select_admins_type1"])
            self.click(self.yaml_data["create_interest_group"]["join_admins"])
            self.click(self.yaml_data["create_interest_group"]["select_admins_submit"])
        elif scope_type == 2:
            self.click(self.yaml_data["create_interest_group"]["designated_department"])
            self.click(self.yaml_data["create_interest_group"]["select_department"])
            self.click(self.yaml_data["create_interest_group"]["research_and_development_department"])
            self.click(self.yaml_data["create_interest_group"]["sales_department"])
            self.click(self.yaml_data["create_interest_group"]["select_department_submit"])
            # ��ӹ���Ա
            ele = self.locator_element(self.yaml_data["create_interest_group"]["admins"])
            js = "arguments[0].scrollIntoView()"
            self.wd.execute_script(js, ele)
            self.click(self.yaml_data["create_interest_group"]["admins"])
            self.click(self.yaml_data["create_interest_group"]["select_admins_type2"])
            self.click(self.yaml_data["create_interest_group"]["join_admins"])
            self.click(self.yaml_data["create_interest_group"]["select_admins_submit"])
        else:
            self.click(self.yaml_data["create_interest_group"]["designated_employees"])
            self.click(self.yaml_data["create_interest_group"]["select_employee"])
            self.click(self.yaml_data["create_interest_group"]["select_employee_9527015"])
            self.click(self.yaml_data["create_interest_group"]["select_employee_9527014"])
            self.click(self.yaml_data["create_interest_group"]["join_employee"])
            self.click(self.yaml_data["create_interest_group"]["select_employee_submit"])
            # ��ӹ���Ա
            ele = self.locator_element(self.yaml_data["create_interest_group"]["admins"])
            js = "arguments[0].scrollIntoView()"
            self.wd.execute_script(js, ele)
            self.click(self.yaml_data["create_interest_group"]["admins"])
            self.click(self.yaml_data["create_interest_group"]["select_admins_type3"])
            self.click(self.yaml_data["create_interest_group"]["join_admins"])
            self.click(self.yaml_data["create_interest_group"]["select_admins_submit"])
        # ����ύ��ť
        self.click(self.yaml_data["create_interest_group"]["submit"])

    # �½���ȤС��ɹ�
    def create_group_success(self):
        return self.get_text(self.yaml_data["create_interest_group"]["create_group_success"])

    # δ��дС�����Ƶ����½�С��ʧ��
    def get_group_name_null_fail(self):
        return self.get_text(self.yaml_data["create_interest_group"]["group_name_null"])

    # δ�ϴ�С�����ͼ�����½�С��ʧ��
    def get_cover_image_null_fail(self):
        return self.get_text(self.yaml_data["create_interest_group"]["cover_image_null"])

    # δ��дС����ܵ����½�С��ʧ��
    def get_introduction_null_fail(self):
        return self.get_text(self.yaml_data["create_interest_group"]["introduction_null"])


if __name__ == '__main__':
    test = CreateIntGroPage('Chrome', "http://192.168.0.139:18091/pbf_company/index.html#/login?redirect=%2Fhome")
    test.login("12138002", "123456", "111111")
    test.create_int_group("С������", "С�����", scope_type=3)
