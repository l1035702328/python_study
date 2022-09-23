# -*- coding: utf-8 -*-
# @Time    : 2022/9/6 11:20
# @Author  : LZZ
# @FileName: 核验姓名与零钱.py
# @Software: PyCharm
import time
from selenium import webdriver

def query_name():
    with open('1.text','r',encoding='utf-8') as f:
        uins = f.read().split(';')

    print(uins)
    len(uins)
    # 查询姓名只有一位数的人
    driver = webdriver.Chrome(executable_path='../chromedriver.exe')
    driver.get("https://iwiki.woa.com/pages/viewpage.action?pageId=1588278945")
    driver.find_element_by_xpath("//*[@id='btn_smartlogin']").click()
    time.sleep(5)
    driver.get('https://xuat.wxp.woa.com/assistant/userAccountDetail?userGroupId=4802929')
    for index, value in enumerate(uins):
        print('当前uin为{},当前执行次数为{}'.format(value, index+1))
        time.sleep(5)
        # 清空输入框
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/section/section/section/section/section/main/div[3]/div[2]/div[2]/input").clear()
        # 输入uin
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/section/section/section/section/section/main/div[3]/div[2]/div[2]/input").send_keys(
            value)
        # 点击查询
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/section/section/section/section/section/main/div[3]/div[2]/button[1]/span").click()
        time.sleep(5)
        # 查看状态是否为构造中
        flag = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/section/section/section/section/section/main/div[3]/div[3]/div[3]/table/tbody/tr/td[4]/div/div").text
        print(flag)
        if not flag:
            time.sleep(10)
            print("载入失败重试")
            flag = driver.find_element_by_xpath(
                "/html/body/div[1]/div/div/section/section/section/section/section/main/div[3]/div[3]/div[3]/table/tbody/tr/td[4]/div/div").text


        if flag == '构造中':
            time.sleep(3)
            # 点击编辑
            driver.find_element_by_xpath(
                "/html/body/div[1]/div/div/section/section/section/section/section/main/div[3]/div[3]/div[4]/div[2]/table/tbody/tr/td[5]/div/button/span/a").click()
            time.sleep(6)
            # 进入页面  #获取输入框文本信息
            name = driver.find_element_by_xpath("/html/body/div[1]/div/div/section/section/section/section/section/main/div[2]/div[4]/div[11]/div[2]/div/input").get_attribute("value")
            balance = driver.find_element_by_xpath(
                "/html/body/div[1]/div/div/section/section/section/section/section/main/div[2]/div[6]/div[5]/div[2]/div/input").get_attribute(
                "value")
            if len(name) <= 1 or int(balance) != 0:
                print("目标身份异常，name为{}:位数为{}".format(name, len(name)))
                # 有问题的uin写入文件 追加模式
                with open('一位数与存在零钱uin.txt', 'a+', encoding='utf-8') as my_file:
                    my_file.write('{},'.format(value))
            else:
                print("name为{}零钱为{}:位数为{},通过".format(name,balance,len(name)))

            # 返回上一页
            time.sleep(1)
            driver.find_element_by_xpath(
                "/html/body/div[1]/div/div/section/section/section/section/section/footer/button/span").click()
        else:
            print("该uin为其他状态")
            with open('其他状态.txt', 'a+', encoding='utf-8') as my_file:
                my_file.write('{};'.format(value))

if __name__ == '__main__':
    query_name()