# coding = utf-8
# 用户输入和while 循环

# 使用函数input() 时，Python将用户输入解读为字符串
if __name__ == '__main__':
    #     old = input("old:")
    #     old = int(old)
    #     if old > 10:
    #         print("old>10")
    #
    # # 求模运算符奇偶性
    #     if old % 2 == 0:
    #         print("目标为偶数")
    #     else:
    #         print("目标为奇数")

    # while 循环
    # 让用户选择退出时间
    # text = ''
    # while text != 'quit':
    #     text = input("input text:")

    # 使用标志
    # flag = True
    # while flag:
    #     msg = input("msg:")
    #     if msg == "quit":
    #         flag = False
    #     else:
    #         print(msg)

    # 使用break退出循环
    # while True:
    #     msg = input("msg:")
    #     if msg == "quit":
    #         break
    #     else:
    #         print(msg)

    # 循环中使用continue 判断奇偶数
    # cou = 0
    # while cou < 10:
    #     cou += 1
    #     if cou % 2 == 0:
    #         continue
    #     print("奇数:{}".format(cou))

    # 使用while 循环处理列表和字典
    # 列表中移动元素
    # unconfirmed_users = ['alice', 'brian', 'candace']
    # unc = []
    # while unconfirmed_users:
    #     temporary = unconfirmed_users.pop()
    #     unc.append(temporary)
    # print(unc)

    # 删除为特定值的所有元素列表
    pets = ["dog", "cat", "tiger", "cock", "cat"]
    while "cat" in pets:
        pets.remove("cat")
    print(pets)



