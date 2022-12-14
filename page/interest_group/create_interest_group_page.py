# coding=gbk
import os
from time import sleep

from common.read_elements_file import ReadElementsFile
from common.read_path_file import ReadPathFile
from page.interest_group.interest_group_page import InterestGroupPage


# 创建兴趣小组页面
class CreateIntGroPage(InterestGroupPage):
    def __init__(self, browser_type, url):
        super().__init__(browser_type, url)
        self.file_path = ReadPathFile()
        self.elements_path = self.file_path.get_elements_file_path()
        self.elements_data = ReadElementsFile()
        self.elements = self.elements_data.read_elements_data(self.elements_path)

    # 新建兴趣小组
    def create_int_group(self, group_name, group_introduction, scope_type):
        interest_groups_ele = self.locator_element(self.elements["home"]["interest_groups"])
        js = "arguments[0].scrollIntoView()"
        self.wd.execute_script(js, interest_groups_ele)
        self.click(self.elements["home"]["interest_groups"])
        self.click(self.elements["interest_group"]["create_group"])

        # 输入小组名称
        self.send_keys(self.elements["create_interest_group"]["group_name"], group_name)
        # 上传小组封面图
        js = "document.getElementsByName('file')[0].setAttribute('style', 'display:block !important')"
        self.transfer_js(js)
        base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        image_path = os.path.join(base_path, r"data\image\1.jpg")
        self.send_keys(self.elements["create_interest_group"]["cover_image"], image_path)
        # 输入小组介绍
        self.send_keys(self.elements["create_interest_group"]["group_introduction"], group_introduction)
        # 选择可见范围并在可见范围内添加管理员
        if scope_type == 1:
            # 可见范围选择全部部门
            self.click(self.elements["create_interest_group"]["all_departments"])
            # 添加管理员
            add_admins_ele = self.locator_element(self.elements["create_interest_group"]["admins"])
            js = "arguments[0].click();"
            self.transfer_js(js, add_admins_ele)
            # 下一行代码会报错：selenium.common.exceptions.ElementClickInterceptedException:
            #       Message: element click intercepted:
            #       Element <>...<> is not clickable at point (635, 791).
            #             Other element would receive the click: <>...<>
            # 可能原因：1.存在JavaScript或AJAX调用，元素未被点击
            #         2.元素未显示在窗口中
            #         3.元素存在但具有永久叠加
            #                 上文的解决办法是针对第三种原因的代码
            # self.click(self.elements["create_interest_group"]["admins"])
            self.click(self.elements["create_interest_group"]["select_admins_type1"])
            self.click(self.elements["create_interest_group"]["join_admins"])
            self.click(self.elements["create_interest_group"]["select_admins_submit"])
        elif scope_type == 2:
            # 可见范围选择指定部门
            self.click(self.elements["create_interest_group"]["designated_department"])
            self.click(self.elements["create_interest_group"]["select_department"])
            self.click(self.elements["create_interest_group"]["research_and_development_department"])
            self.click(self.elements["create_interest_group"]["sales_department"])
            self.click(self.elements["create_interest_group"]["select_department_submit"])
            # 添加管理员
            add_admins_ele = self.locator_element(self.elements["create_interest_group"]["admins"])
            js = "arguments[0].scrollIntoView()"
            self.transfer_js(js, add_admins_ele)
            self.click(self.elements["create_interest_group"]["admins"])
            self.click(self.elements["create_interest_group"]["select_admins_type2"])
            self.click(self.elements["create_interest_group"]["join_admins"])
            self.click(self.elements["create_interest_group"]["select_admins_submit"])
        else:
            # 可见范围选择指定员工
            self.click(self.elements["create_interest_group"]["designated_employees"])
            self.click(self.elements["create_interest_group"]["select_employee"])
            self.click(self.elements["create_interest_group"]["select_employee_9527015"])
            self.click(self.elements["create_interest_group"]["select_employee_9527014"])
            self.click(self.elements["create_interest_group"]["join_employee"])
            self.click(self.elements["create_interest_group"]["select_employee_submit"])
            # 添加管理员
            add_admins_ele = self.locator_element(self.elements["create_interest_group"]["admins"])
            js = "arguments[0].scrollIntoView()"
            self.transfer_js(js, add_admins_ele)
            self.click(self.elements["create_interest_group"]["admins"])
            self.click(self.elements["create_interest_group"]["select_admins_type3"])
            self.click(self.elements["create_interest_group"]["join_admins"])
            self.click(self.elements["create_interest_group"]["select_admins_submit"])
        # 点击提交按钮
        self.click(self.elements["create_interest_group"]["submit"])
        sleep(5)

    # 新建兴趣小组成功
    def create_group_success(self):
        return self.get_text(self.elements["create_interest_group"]["create_group_success"])

    # 未填写小组名称导致新建小组失败
    def get_group_name_null_fail(self):
        return self.get_text(self.elements["create_interest_group"]["group_name_null"])

    # 未上传小组封面图导致新建小组失败
    def get_cover_image_null_fail(self):
        return self.get_text(self.elements["create_interest_group"]["cover_image_null"])

    # 未填写小组介绍导致新建小组失败
    def get_introduction_null_fail(self):
        return self.get_text(self.elements["create_interest_group"]["introduction_null"])


if __name__ == '__main__':
    test = CreateIntGroPage('Chrome', "http://192.168.0.139:18091/pbf_company/index.html#/login?redirect=%2Fhome")
    test.login("12138002", "123456", "111111")
    test.create_int_group("小组名称", "小组介绍", scope_type=1)
