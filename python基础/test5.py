# coding = utf -8

# 汇总

# import copy
#
# # 字符串的内置函数
# zif = "\t\t\t\nasdf\t\t\t "
# print(zif.lstrip())
# print(zif.rstrip())
# print(zif.strip())
#
# zfc1 = "hello world"
# print(zfc1.upper())
# print(zfc1.lower())
# print(zfc1.title())
#
#
# a = [1, 3, 5]
# # b = a  # 直接赋值
# b = a[:]  # 浅拷贝
# b = copy.deepcopy(a) # 深拷贝
# if a is b:
#     print("比较引用为相等")
# else:
#     print("不等")


# if elif
# a = 2
# b = 1
# if a>b:
#     print("a>b")
# elif a>b:
#     print("a>b")
# else:
#     print("ni")

# 判断列表为空 因为对于一个空的list，它的真值永远都是False。用 len 函数检查list里面元素的长度为0来判断是否为空是多此一举
# 同样的道理可以衍生到元组(不可变) 字典 集合上
# liebiao = []
# zifuchuan= ''
# shuzi = 0
# kong = None
# if liebiao == zifuchuan:
#     print("为空")
# else:
#     print("没")
#


# 练习5-10：检查用户名 按下面的说明编写一个程序，模拟
# 网站如何确保每位用户的用户名都独一无二。
# 创建一个至少包含5个用户名的列表，并将其命名
# 为current_users 。
# 再创建一个包含5个用户名的列表，将其命名
# 为new_users ，并确保其中有一两个用户名也包含在列
# 表current_users 中。
# 遍历列表new_users ，对于其中的每个用户名，都检查它
# 是否已被使用。如果是，就打印一条消息，指出需要输入
# 别的用户名；否则，打印一条消息，指出这个用户名未被
# 使用。
# 确保比较时不区分大小写。换句话说，如果用户
# 名'John' 已被使用，应拒绝用户名'JOHN' 。（为此，需
# 要创建列表current_users 的副本，其中包含当前所有
# 用户名的小写版本。
current_users = ["li", 'zhou', "ZHANG", "Liu", "hu"]
new_users = ["Li", "Liu", "zhen", "zhou", "HUANg"]
for new_user in new_users:
    if new_user.lower() in (j.lower() for j in current_users):
        print("{} use".format(new_user))
    else:
        print("{} no use".format(new_user))















