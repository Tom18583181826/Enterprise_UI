from common.read_elements_file import ReadYaml
from common.read_path_file import ReadIni
from page.login_page import LoginPage


# 首页页面
class HomePage(LoginPage):
    def __init__(self, browser_type, url):
        super().__init__(browser_type, url)
        self.read_ini = ReadIni()
        self.yaml_path = self.read_ini.get_yaml_file_path()
        self.read_yaml = ReadYaml()
        self.yaml_data = self.read_yaml.read_yaml_data(self.yaml_path)

    # 点击通讯录图标，快捷进入通讯录页面
    def address_book(self):
        self.click(self.yaml_data["home"]["address_book"])

    # 点击福利签收记录图标，快捷进入福利签收记录页面
    def benefit_sign_up_records(self):
        self.click(self.yaml_data["home"]["benefit_sign_up_records"])

    # 点击高德打车图标，快捷进入高德打车页面
    def gaode_take_taxi(self):
        self.click(self.yaml_data["home"]["gaode_take_taxi"])

    # 点击积分签到图标，快捷进入积分签到页面
    def points_Sign_in(self):
        self.click(self.yaml_data["home"]["points_Sign_in"])

    # 点击积分抽奖图标，快捷进入积分抽奖页面
    def point_sweepstakes(self):
        self.click(self.yaml_data["home"]["point_sweepstakes"])

    # 点击健步走图标，快捷进入健步走页面
    def walking(self):
        self.click(self.yaml_data["home"]["walking"])

    # 点击公告管理图标，快捷进入公告管理页面
    def announcement_management(self):
        self.click(self.yaml_data["home"]["announcement_management"])

    # 点击工会信箱图标，快捷进入工会信箱页面
    def trade_union_mailbox(self):
        self.click(self.yaml_data["home"]["trade_union_mailbox"])

    # 点击积分发放记录图标，快捷进入积分发放记录页面
    def points_issuance_record(self):
        self.click(self.yaml_data["home"]["points_issuance_record"])

    # 点击企业云盘图标，快捷进入企业云盘页面
    def enterprise_cloud_drive(self):
        self.click(self.yaml_data["home"]["enterprise_cloud_drive"])

    # 点击活动报名图标，快捷进入活动报名页面
    def event_registration(self):
        self.click(self.yaml_data["home"]["event_registration"])

    # 点击员工关怀图标，快捷进入员工关怀页面
    def employee_care(self):
        self.click(self.yaml_data["home"]["employee_care"])

    # 点击荣誉墙图标，快捷进入荣誉墙页面
    def wall_of_honor(self):
        self.click(self.yaml_data["home"]["wall_of_honor"])

    # 点击闯关答题图标，快捷进入闯关答题页面
    def breakout_quiz(self):
        self.click(self.yaml_data["home"]["breakout_quiz"])

    # 点击员工调研图标，快捷进入员工调研页面
    def employee_research(self):
        self.click(self.yaml_data["home"]["employee_research"])

    # 点击活动投票图标，快捷进入活动投票页面
    def event_voting(self):
        self.click(self.yaml_data["home"]["event_voting"])

    # 点击兴趣小组图标，快捷进入兴趣小组页面
    def interest_groups(self):
        self.click(self.yaml_data["home"]["interest_groups"])


if __name__ == '__main__':
    click_obj = HomePage('Chrome', "http://192.168.0.139:18091/pbf_company/index.html#/login?redirect=%2Fhome")
    click_obj.login("12138002", "123456", "111111")
    click_obj.address_book()
