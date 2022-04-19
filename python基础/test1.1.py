# coding = utf-8
import copy

if __name__ == '__main__':

    # # 深拷贝浅拷贝
    # aa1 = [1, 3, 5]
    # bb1 = aa1  # 直接指向了aa1 的子对象 aa1->0x01->0xxx  bb1->0x01->0xxx
    # bb2 = copy.copy(aa1)  # 将aa1对象的引用赋给新对象 aa1->0x01->0xxx bb1->0x02->0xxx
    # bb3 = copy.deepcopy(aa1)  # 生成一个新对象
    # aa1.append(7)
    # print(aa1)
    # print(bb1)
    # print(bb2)
    # print(bb3)


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
    aa.sort()
    print(aa)
    # 相反排序
    aa.sort(reverse=True)
    print(aa)
    # 临时排序
    bb = [3, 5, 1]
    print(sorted(bb))
    print(bb)
    # 倒着打印
    bb.reverse()
    print(bb)
    # 确定长度
    print(len(bb))
    # 索引
    print(bb[-1])
