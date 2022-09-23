# -*- coding: utf-8 -*-
# @Time    : 2022/7/13 15:23
# @Author  : LZZ
# @FileName: 批量构造中.py
# @Software: PyCharm

import time
from selenium import webdriver

if __name__ == '__main__':

    with open('1.text', 'r', encoding='utf-8') as f:
        uins = f.read().split(';')
    print("共有{}个uin,为{}".format(len(uins),uins))
    driver = webdriver.Chrome()
    driver.get("https://iwiki.woa.com/pages/viewpage.action?pageId=1588278945")
    driver.find_element_by_xpath("//*[@id='btn_smartlogin']").click()
    time.sleep(5)
    driver.get('https://xuat.wxp.woa.com/assistant/userAccountDetail?userGroupId=4802929')
    for _ in uins:
        print('当前uin为{}'.format(_))
        time.sleep(5)
        # 清空输入框
        driver.find_element_by_xpath("/html/body/div[1]/div/div/section/section/section/section/section/main/div[3]/div[2]/div[2]/input").clear()
        # 输入uin
        driver.find_element_by_xpath("/html/body/div[1]/div/div/section/section/section/section/section/main/div[3]/div[2]/div[2]/input").send_keys(_)
        # 点击查询
        driver.find_element_by_xpath("/html/body/div[1]/div/div/section/section/section/section/section/main/div[3]/div[2]/button[1]/span").click()
        time.sleep(5)
        # 查看状态是否为构造中
        flag = driver.find_element_by_xpath("/html/body/div[1]/div/div/section/section/section/section/section/main/div[3]/div[3]/div[3]/table/tbody/tr/td[4]/div/div").text
        print(flag)
        if flag == '构造中':
            continue
        else:
            time.sleep(3)
        # 点击编辑
            driver.find_element_by_xpath("/html/body/div[1]/div/div/section/section/section/section/section/main/div[3]/div[3]/div[4]/div[2]/table/tbody/tr/td[5]/div/button/span/a").click()
            time.sleep(5)
        # 进入生效页面  #点击选择框
            driver.find_element_by_xpath("/html/body/div[1]/div/div/section/section/section/section/section/main/div[2]/div[2]/div/div/input").click()
        # 修正为构造中
            time.sleep(2)
            driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/ul/li[1]").click()
        # 点击提交 提交后回到首页 继续循环
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/div[1]/div/div/section/section/section/section/section/footer/span/span/button/span").click()
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/button[2]/span").click()
            print("回到首页执行下一次循环")
        # 正常修正得uin写入文件 追加模式
            with open('xiuzhen.txt','a+',encoding='utf-8') as my_file:
                my_file.write('{};'.format(_))