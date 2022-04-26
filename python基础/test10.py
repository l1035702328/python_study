# coding = utf-8
def read_file():
    with open("text1.txt") as f:
        # f已读取第一行内容
        text = f.readline()
        # 再遍历f下标已经到了第二行
        for i in f:
            print(i)
    print(text)


def read_file1():
    with open("text1.txt") as f:
        # f已读取第一行内容
        text = f.readlines()
# 每行的末尾都有一
# 个看不见的换行符，而函数调用print() 也会加上一个换行符，因
# 此每行末尾都有两个换行符
    for i in text:
        print(i.rstrip())


def write_file():
    with open("text1.txt", "w") as f:
        f.write("hi\n")
        f.write("i im liyunlong\n")
        f.write("can i help you?\n")

# 附加
def write_file1():
    with open("text1.txt", "a") as f:
        f.write("nihao\n")


if __name__ == '__main__':
    write_file1()