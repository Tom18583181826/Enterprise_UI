# coding=gbk
# ���н�����뱨��(��������:SyntaxError: Non-UTF-8 code starting with '\xb9' in file,����ĸ�Դ���Ǵ�����������ע�͵��±�������)
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# ��¼Ψ����ѡ����ϵͳ
driver.get("http://wa.demo.sclonsee.com/")
driver.maximize_window()

# ͨ�����Cookie������¼��ֱ֤�ӵ�¼(ǰ����Cookie��ʧЧ):
# 1��������ͨ��ץ�����ߵȻ�ȡCookie
# 2��ͨ��Selenium�ṩ��add_cookie()�������Cookie��Ϣ,����Cookie�ֶ�����
driver.add_cookie({"name": "advanced-backend", "value": "9dv872hpqagg0pbq1rsn5a7i53"})
driver.add_cookie({"name": "_identity-backend",
                   "value": "0007be3bc00303df5e8948e39a7528adbb4027892890c531425096f01c7cabdaa%3A2%3A%7Bi%3A0%3Bs%3A17%3A%22_identity-backend%22%3Bi%3A1%3Bs%3A43%3A%22%5B1%2C%22hRJ6Az_SgAckqltCzUSEcGEuDv1MfbsT%22%2C7200%5D%22%3B%7D"})
driver.add_cookie({"name": "_csrf-backend",
                   "value": "80b39f8d26989b28828a01ccf0909635833e38f33674102bbb1d7520f441cf71a%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22_csrf-backend%22%3Bi%3A1%3Bs%3A32%3A%22o302IcjERYZSmVH3bUwWu1OG9z_BU29G%22%3B%7D"})

sleep(3)
driver.refresh()
# ˢ��ҳ�棬�鿴�Ƿ��¼�ɹ�
sleep(3)

# ��ȡ��¼�û�������ӡ
username = driver.find_element(by=By.CLASS_NAME, value="hidden-xs").text
print(username)

# �ر������
driver.quit()

# WebDriver���ò���Cookie�ķ����У�
# get_cookies():��ȡ���е�Cookie
# get_cookie(name):�����ֵ���keyΪname��Cookie
# add_cookie(dict):���Cookie
# delect_cookie(name, optionString):ɾ����ΪoptionString��Cookie
# delect_all_cookies():ɾ������Cookie
