# -*- coding: utf-8 -*-
# @Time    : 2022/9/6 14:09
# @Author  : LZZ
# @FileName: 批量生效.py
# @Software: PyCharm
import time
from selenium import webdriver


def shenxiao():
    with open('../1.text', 'r', encoding='utf-8') as f:
        uins = f.read().split(';')
    print("共有{}个uin,为{}".format(len(uins), uins))
    driver = webdriver.Chrome(executable_path="../chromedriver.exe")
    driver.get("https://iwiki.woa.com/pages/viewpage.action?pageId=1588278945")
    driver.find_element_by_xpath("//*[@id='btn_smartlogin']").click()
    time.sleep(5)
    driver.get('https://xuat.wxp.woa.com/assistant/userAccountDetail?userGroupId=4802929')

    for index, value in enumerate(uins):
        try:
            print('当前uin为{} 当前进度为{}'.format(value, index))
            time.sleep(10)
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
            if flag == '构造中':
                time.sleep(3)
                # 点击编辑
                driver.find_element_by_xpath(
                    "/html/body/div[1]/div/div/section/section/section/section/section/main/div[3]/div[3]/div[4]/div[2]/table/tbody/tr/td[5]/div/button/span/a").click()
                time.sleep(5)
                # 获取零钱余额
                balance = driver.find_element_by_xpath("/html/body/div[1]/div/div/section/section/section/section/section/main/div[2]/div[6]/div[5]/div[2]/div/input").get_attribute("value")
                # 获取用户名字
                name = driver.find_element_by_xpath(
                    "/html/body/div[1]/div/div/section/section/section/section/section/main/div[2]/div[4]/div[11]/div[2]/div/input").get_attribute(
                    "value")
                if balance and name:
                    print("用户uin:{} 余额为:{} 姓名为:{}".format(value,balance,name))
                    if int(balance) == 9999900 and len(name) > 1:
                        print("核验成功 可生效")
                        # 进入生效页面  #点击选择框
                        driver.find_element_by_xpath(
                            "/html/body/div[1]/div/div/section/section/section/section/section/main/div[2]/div[2]/div/div/input").click()
                        # 修正为生效
                        time.sleep(2)
                        driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/ul/li[2]/span").click()
                        # 保存两张银行卡信息
                        time.sleep(2)
                        driver.find_element_by_xpath("/html/body/div[1]/div/div/section/section/section/section/section/main/div[4]/div[2]/div/div[3]/table/tbody/tr[1]/td[8]/div/a").click()
                        time.sleep(5)
                        driver.find_element_by_xpath("/html/body/div[1]/div/div/section/section/section/section/section/main/div[4]/div[2]/div/div[3]/table/tbody/tr[2]/td[8]/div/a").click()
                        time.sleep(3)
                        # 检查用户属性
                        driver.find_element_by_xpath("/html/body/div[1]/div/div/section/section/section/section/section/footer/button[2]").click()
                        # 点击返回
                        time.sleep(3)
                        driver.find_element_by_xpath("/html/body/div[1]/div/div/section/section/section/section/section/div/div/div[1]/button/i").click()
                        time.sleep(3)
                        # 点击提交 提交后回到首页 继续循环
                        driver.find_element_by_xpath(
                            "/html/body/div[1]/div/div/section/section/section/section/section/footer/span/span/button/span").click()
                        time.sleep(1)
                        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/button[2]/span").click()
                        print("回到首页执行下一次循环")
                        continue
                    else:
                        driver.find_element_by_xpath(
                            "/html/body/div[1]/div/div/section/section/section/section/section/footer/button/span").click()
                        with open("yichan.text", "a+", encoding='utf-8') as f:
                            print("异常uin{}".format(value))
                            f.write("{},".format(value))

                else:
                    with open("yichan.text", "a+", encoding='utf-8') as f:
                        print("校验未通过uin{}".format(value))
                        f.write("{},".format(value))
                    driver.find_element_by_xpath(
                        "/html/body/div[1]/div/div/section/section/section/section/section/footer/button/span").click()


        except Exception as e:
            print(e)
            with open("yichan.text", "a+",encoding='utf-8')as f:
                print("异常uin{}".format(value))
                f.write("{},".format(value))
            if driver.find_element_by_xpath("/html/body/div[1]/div/div/section/section/section/section/section/footer/button/span"):
                driver.find_element_by_xpath("/html/body/div[1]/div/div/section/section/section/section/section/footer/button/span").click()

if __name__ == '__main__':
    shenxiao()