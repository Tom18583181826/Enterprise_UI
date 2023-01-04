from selenium.webdriver import Keys

from common.read_elements_file import ReadElementsFile
from common.read_path_file import ReadPathFile
from page.interest_group.member_list_page import MemberListPage


# 成员详情页面
class MenberDetailsPage(MemberListPage):
    def __init__(self, browser_type, url):
        super().__init__(browser_type, url)
        self.file_path = ReadPathFile()
        self.elements_path = self.file_path.get_elements_file_path()
        self.elements_data = ReadElementsFile()
        self.elements = self.elements_data.read_elements_data(self.elements_path)

    # 选择帖子类型查询
    def post_type_query(self, post_type):
        self.click(self.elements["member_details"]["post_type"])
        if post_type == 1:
            self.click(self.elements["member_details"]["text_type"])
        elif post_type == 2:
            self.click(self.elements["member_details"]["image_type"])
        else:
            self.click(self.elements["member_details"]["text_and_image"])

    # 发表时间查询
    def publish_time_query(self, start_time, stop_time):
        self.send_keys(self.elements["member_details"]["start_time"], start_time)
        self.send_keys(self.elements["member_details"]["stop_time"], stop_time)
        ele = self.locator_element(self.elements["member_details"]["stop_time"])
        ele.send_keys(Keys.ENTER)

    # 发表顺序查询
    def publication_order_query(self, order_type):
        self.click(self.elements["member_details"]["publication_order"])
        if order_type == 1:
            self.click(self.elements["member_details"]["order_type"])
        else:
            self.click(self.elements["member_details"]["reverse_type"])

    # 查询已删除帖子
    def delete_post_query(self):
        self.click(self.elements["member_details"]["delete_post_query"])

    # 批量删除按钮
    def batch_delete(self):
        self.click(self.elements["member_details"]["batch_delete"])

    # 查看帖子详情
    def view_details(self):
        self.click(self.elements["member_details"]["view_details"])

    # 置顶/取消置顶
    def sticky(self):
        self.click(self.elements["member_details"]["sticky"])

    # 删除按钮
    def delete_button(self):
        self.click(self.elements["member_details"]["delete_button"])

    # 进入已参与活动页面
    def participated_activities(self):
        self.click(self.elements["member_details"]["participated_activities"])

    # 活动类型查询
    def event_type_query(self, event_type):
        self.click(self.elements["member_details"]["event_type"])
