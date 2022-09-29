# coding=gbk
# https://www.cnblogs.com/stillwalking/p/13902833.html
import re  # ��������
from PIL import Image  # ���ڴ�ͼƬ�Ͷ�ͼƬ����
import pytesseract  # ����ͼƬת����
from selenium import webdriver  # ���ڴ���վ
import time  # ��������ͣ��


class VerificationCode:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.find_element = self.driver.find_element_by_class_name

    def get_pictures(self):
        self.driver.get('https://vmall.vmall888.com')  # �򿪵�½ҳ��
        self.driver.maximize_window()
        self.driver.save_screenshot(
            r'J:\����ʾ��\UIAutomationCode\UIAutomationTest\data\login_screenshot\login_screenshot.png')  # ȫ����ͼ
        page_snap_obj = Image.open(
            r'J:\����ʾ��\UIAutomationCode\UIAutomationTest\data\login_screenshot\login_screenshot.png')
        img = self.find_element("yanmimg")  # ��֤��Ԫ��λ��
        time.sleep(1)
        location = img.location
        size = img.size  # ��ȡ��֤��Ĵ�С����
        left = location['x']
        top = location['y']
        right = left + size['width']
        bottom = top + size['height']
        image_obj = page_snap_obj.crop((left, top, right, bottom))  # ������֤��ĳ����и���֤��
        image_obj.show()  # ���и���������֤��
        self.driver.close()  # ��������֤���ر������
        return image_obj

    def processing_image(self):
        image_obj = self.get_pictures()  # ��ȡ��֤��
        img = image_obj.convert("L")  # ת�Ҷ�
        pixdata = img.load()
        w, h = img.size
        threshold = 160
        # �����������أ�������ֵ��Ϊ��ɫ
        for y in range(h):
            for x in range(w):
                if pixdata[x, y] < threshold:
                    pixdata[x, y] = 0
                else:
                    pixdata[x, y] = 255
        return img

    def delete_spot(self):
        images = self.processing_image()
        data = images.getdata()
        w, h = images.size
        black_point = 0
        for x in range(1, w - 1):
            for y in range(1, h - 1):
                mid_pixel = data[w * y + x]  # �������ص�����ֵ
                if mid_pixel < 50:  # �ҳ����������ĸ��������ص�����ֵ
                    top_pixel = data[w * (y - 1) + x]
                    left_pixel = data[w * y + (x - 1)]
                    down_pixel = data[w * (y + 1) + x]
                    right_pixel = data[w * y + (x + 1)]
                    # �ж��������ҵĺ�ɫ���ص��ܸ���
                    if top_pixel < 10:
                        black_point += 1
                    if left_pixel < 10:
                        black_point += 1
                    if down_pixel < 10:
                        black_point += 1
                    if right_pixel < 10:
                        black_point += 1
                    if black_point < 1:
                        images.putpixel((x, y), 255)
                    black_point = 0
        # images.show()
        return images

    def image_str(self):
        image = self.delete_spot()
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # ����pyteseract·��
        result = pytesseract.image_to_string(image)  # ͼƬת����
        resultj = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", result)  # ȥ��ʶ������������ַ�
        result_four = resultj[0:4]  # ֻ��ȡǰ4���ַ�
        # print(resultj)  # ��ӡʶ�����֤��
        return result_four


if __name__ == '__main__':
    a = VerificationCode()
    a.get_pictures()
