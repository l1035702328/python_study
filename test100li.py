# coding = utf -8
# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
def test1():
    num = 0
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if i != j and j != k and k != i:
                    print("{}{}{}".format(i, j, k))
                    num  +=1
    print(num)

# 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
# 低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，
# 可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，
# 可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
def test2():
    money = int(input("当月利润I:"))
    if money <= 100000:
        money = money * 0.1
    elif money <= 200000:
        money = money * 0.075
    elif money <= 400000:
        money = money * 0.05
    elif money <= 600000:
        money = money * 0.03
    elif money <= 1000000:
        money = money * 0.015
    elif money > 1000000:
        money = money * 0.01
    return money

if __name__ == '__main__':
    print(test2())