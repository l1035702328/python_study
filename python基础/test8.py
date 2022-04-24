# coding = utf-8
#
def test1(name, old):
    print("hello,{},you old is {}".format(name, old))


# 默认值
def test2(name="hechenlong"):
    print(name)


# 等效的函数调用
def test3(name, old=15):
    print(name)
    print(old)

def test4(f1, f2,  f3=""):
    print("实参可选{}{}{}".format(f1, f2, f3))


# 列表修改简洁
def test5(lists):
    new_lists = []
    while lists:
        new_lists.append(lists.pop())
    return new_lists


#  传递任意数量的实参 实际就是将实参封装到了一个元组中
def test6(*top):
    print("{}:{}".format(type(top), top))


# 结合使用位置实参和任意数量实参
def test7(name, *top):
    print(name)
    for i in top:
        print(i)


# 使用任意数量的关键字实参 实际是字典
def test8(name, old, **user_info):
    print("{}:\t{}".format(type(user_info), user_info))


if __name__ == '__main__':
    # 位置实参
    test1("liyunlong", 15)
    # 关键字实参
    test1(old=13, name="zhaozilong")
    # 默认值
    test2()
    # 等效的函数调用
    test3(1, 3)
    test4(1, 2)
    # 列表修改简洁
    print(test5([1, 3, 5, 7, 9]))
    # 禁止函数修改列表 # 浅拷贝副本
    list_a = [1, 3, 5, 7, [1, 3]]
    print(test5(list_a[:]))
    print(list_a)
    # 传递任意数量的实参
    test6("hello", "world")
    # 结合使用位置实参和任意数量实参
    test7("liyunlong", 1, 5, 6)
    # 使用任意数量的关键字实参
    test8("lixiaolong", 13, name2="lilianjie", name3="lishimin")