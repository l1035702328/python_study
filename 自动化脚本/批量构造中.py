# -*- coding: utf-8 -*-
# @Time    : 2022/7/13 15:23
# @Author  : LZZ
# @FileName: 批量构造中.py
# @Software: PyCharm
import time

import selenium
from selenium import webdriver
import os
if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print("11" + BASE_DIR)
    # driver = webdriver.Chrome()
    # driver.get("https://iwiki.woa.com/pages/viewpage.action?pageId=1588278945")
    # driver.find_element_by_xpath("//*[@id='btn_smartlogin']").click()
    # time.sleep(5)
    # driver.get('http://xuat.wxp.woa.com/assistant/userAccountDetail?userGroupId=4803004')