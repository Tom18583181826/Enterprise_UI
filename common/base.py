import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


# 测试基类，封装的公共方法
class Base:
    # 选择浏览器类型并进入网址
    def __init__(self, browser_type, url):
        if browser_type == "Chrome":
            self.wd = webdriver.Chrome()
        elif browser_type == "Firefox":
            self.wd = webdriver.Firefox()
        elif browser_type == "Edge":
            self.wd = webdriver.Edge()
        else:
            raise TypeError("浏览器类型错误，请输入正确的浏览器类型！！！")
        self.wd.get(url)
        self.wd.maximize_window()

    # 元素定位，判断使用何种元素定位方法
    def selector_to_locator(self, selector):
        selector_type = selector.split(",")[0].strip()
        selector_value = selector.split(",")[1].strip()
        if selector_type == "i" or selector_type == "ID":
            locator = (By.ID, selector_value)
        elif selector_type == "n" or selector_type == "NAME":
            locator = (By.NAME, selector_value)
        elif selector_type == "tag" or selector_type == "TAG_NAME":
            locator = (By.TAG_NAME, selector_value)
        elif selector_type == "class" or selector_type == "CLASS_NAME":
            locator = (By.CLASS_NAME, selector_value)
        elif selector_type == "link" or selector_type == "LINK_TEXT":
            locator = (By.LINK_TEXT, selector_value)
        elif selector_type == "plt" or selector_type == "PARTIAL_LINK_TEXT":
            locator = (By.PARTIAL_LINK_TEXT, selector_value)
        elif selector_type == "x" or selector_type == "XPATH":
            locator = (By.XPATH, selector_value)
        elif selector_type == "css" or selector_type == "CSS_SELECTOR":
            locator = (By.CSS_SELECTOR, selector_value)
        else:
            raise TypeError(selector_type + "是无效的，请输入正确的定位方式！！！")
        return locator

    # 设置显式等待控制查找元素的时间---单个元素
    def locator_element(self, selector):
        locator = self.selector_to_locator(selector)
        if locator is not None:
            element = WebDriverWait(self.wd, 10).until(EC.visibility_of_element_located(locator),
                                                       message="元素查找超时！！！")
        else:
            raise ValueError("请输入有效的选择器选择目标元素！！！")
        return element

    # 设置显示等待来控制查找元素的时间---多个元素
    def locator_elements(self, selector):
        locator = self.selector_to_locator(selector)
        if locator is not None:
            elements = self.wd.find_elements(*locator)
        else:
            raise NameError("请输入有效的选择器选择目标元素！！！")
        return elements

    # 模拟按键输入
    def send_keys(self, selector, value):
        input_value = self.locator_element(selector)
        input_value.clear()
        input_value.send_keys(value)

    # 单击元素
    def click(self, selector):
        self.locator_element(selector).click()

    # 提交表单
    def submit(self, selector):
        self.locator_element(selector).submit()

    # 进入iframe框架
    def switch_to_frame(self, selector):
        frame_ele = self.locator_element(selector)
        self.wd.switch_to.frame(frame_ele)

    # 退到iframe框架的上一层
    def switch_to_parent_frame(self):
        self.wd.switch_to.parent_frame()

    # 退到iframe框架的最外层
    def switch_to_default_content(self):
        self.wd.switch_to.default_content()

    # 通过文本定位select下拉框选项
    def select_by_visible_text(self, selector, text):
        Select(self.locator_element(selector)).select_by_visible_text(text)

    # 通过下标索引定位select下拉框选项
    def select_by_index(self, selector, num):
        Select(self.locator_element(selector)).select_by_index(num)

    # 通过value值定位select下拉框选项
    def select_by_value(self, selector, value):
        Select(self.locator_element(selector)).select_by_value(value)

    # 二次定位，适用于有按钮选择的情况
    def second_locator_element(self, selector1, selector2):
        locator1 = self.selector_to_locator(selector1)
        locator2 = self.selector_to_locator(selector2)
        eles = self.wd.find_element(*locator1).find_elements(*locator2)
        random.choice(eles).click()

    # 获取单个元素文本，可以用于断言
    def get_text(self, selector):
        return self.locator_element(selector).text

    # 获取多个元素文本
    def get_texts(self, selector):
        eles = self.locator_elements(selector)
        text_list = []
        for ele in eles:
            text = ele.text
            text_list.append(text)
        return text_list

    # 警告框处理
    def switch_to_alert(self, method):
        alert = self.wd.switch_to.alert
        if method == "text":
            return alert.text
        if method == "accept":
            return alert.accept()
        if method == "dismiss":
            return alert.dismiss()

    # 窗口截图
    def get_screenshot(self, filename):
        self.wd.save_screenshot(filename)

    # 退出浏览器进程
    def quit(self):
        self.wd.quit()

    # 关闭浏览器的某个窗口
    def close(self):
        self.wd.close()

    # 返回元素的属性值，可以是id,name等任意属性
    def get_attribute(self, selector, type_name):
        return self.locator_element(selector).get_attribute(type_name)

    # 返回元素是否可见，可见为True
    def get_is_displayed(self, selector):
        return self.locator_element(selector).is_displayed()

    # 获取当前页面的标题,可以用于断言
    def get_page_title(self):
        return self.wd.title

    # 获取当前页面的URL，可以用于断言
    def get_page_url(self):
        return self.wd.current_url

    # 上传文件,适用于前端使用input标签实现文件上传的场景
    def up_file(self, selector, up_file_path):
        return self.locator_element(selector).send_keys(up_file_path)

    # 调用JavaScript，可以实现浏览器滚动条的拖动和textarea文本框的输入等操作
    def transfer_js(self, js, args=None):
        self.wd.execute_script(js, args)

    # 处理H5视频播放
    def video(self, selector, video_type):
        video = self.locator_element(selector)
        if video_type == "play":
            self.wd.execute_script("arguments[0].play()", video)
        elif video_type == "pause":
            self.wd.execute_script("arguments[0].pause()", video)
        elif video_type == "load":
            self.wd.execute_script("arguments[0].load()", video)
        else:
            self.wd.execute_script("return arguments[0].currentSrc;", video)
