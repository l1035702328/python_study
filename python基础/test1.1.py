# coding = utf-8
import copy

if __name__ == '__main__':
    # # 大小写转换
    # name = "HelloWorld haha"
    # print(name.upper())
    # print(name.lower())
    # print(name.title())
    #
    # # \n换行符 \t制表符
    # print("ni\thao")
    # print("ni\nhao")
    #
    # # 删除空白
    # kongbai = "   bu wei  "
    # print(kongbai.rstrip())  # 末尾
    # print(kongbai.lstrip())  # 开头
    # print(kongbai.strip())  # 两边
    #
    # # 数 无论是哪种运算，只要有操作数是浮点数，Python默认得到的总是浮点 整数相除总是得到浮点数
    # a = 4 / 2
    # print(a)
    #
    # # 用全大小表示常量
    # MAX_CONNECTIONS = 5000
    #
    # # 列表
    # aa = [1, 3, 5, 7, 9]
    # aa.append(10)
    # print(aa)
    # # 添加
    # aa.insert(3, "hello")
    # print(aa)
    # # del删除
    # del aa[0]
    # print(aa)
    # # pop删除 返回了你删除的数值
    # dd = aa.pop()
    # print(aa)
    # # remove 查找数值删除
    # aa.remove("hello")
    # print(aa)

    # 列表排序
    # 组织列表
    aa = ["c", "d", "a", "b"]
    # 按字母排序
    # list.sort() 和 sorted() 都有一个 key 形参用来指定在进行比较前要在每个列表元素上调用的函数（或其他可调用对象）。
    aa.sort()
    print(aa)
    # 相反排序
    aa.sort(reverse=True)
    print(aa)
    # 临时排序
    bb = [3, 5, 1]
    print(sorted(bb))
    print(bb)
    # 倒着排序(不按字母)
    bb.reverse()
    print(bb)
    # 倒着临时排序
    bb.__reversed__()
    # 确定长度
    print(len(bb))
    # 索引
    print(bb[-1])
