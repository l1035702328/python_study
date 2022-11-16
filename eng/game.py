# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 10:19
# @Author  : LZZ
# @FileName: game.py
# @Software: PyCharm

import re
import random
import os

# __只允许这个类（self）自身访问。这种命名的方式更多的是用在类的继承，通过两个下划线开头命名的成员，可以防止被子类重写
# _私有 子类可访问


class EngGame:
    def __init__(self, score=0):
        self.score = score

    def _train_run(self, random_list, relist):
        mistake = []
        for i in random_list:
            for _ in range(100):
                print(relist[i].group("mean"))
                print("\n\n\n\n\n\n\n\n\n\n\n\n")
                print(self.score)
                print("present is {}".format(relist[i].group('present').lower()))
                past = input("input past:")
                print(past)
                if past.lower() == relist[i].group('past').lower():
                    print("you are right")
                else:
                    mistake.append(relist[i])
                    print("sorry,you die")
                    print("present:{},past:{},past_participle:{},mean:{}".format(relist[i].group("present").lower(),
                                                                                 relist[i].group("past"),
                                                                                 relist[i].group("past_participle"),
                                                                                 relist[i].group("mean")))
                    input("任意键继续")
                    continue
                past_participle = input("input past_participle:")
                print(past_participle)
                if past_participle.lower() == relist[i].group('past_participle').lower():
                    print('you are right')
                    print("present:{},past:{},past_participle:{},mean:{}".format(
                        relist[i].group("present").lower(),
                        relist[i].group("past"),
                        relist[i].group("past_participle"),
                        relist[i].group("mean")))
                    self.score += 1
                    break
                else:
                    mistake.append(relist[i])
                    print('sorry,you die')
                    print("present:{},past:{},past_participle:{},mean:{}".format(relist[i].group("present").lower(),
                                                                                 relist[i].group("past"),
                                                                                 relist[i].group("past_participle"),
                                                                                 relist[i].group("mean")))
                    input("任意键继续")
                    continue
        return mistake

    # 游戏模式
    def run(self):
        relist =[]
        with open('buguize.txt',encoding='utf-8') as f:
            str_list = f.readlines()
        for _ in str_list:
            # print(re.search('.*\s–',_,flags=re.I).group(0))
            relist.append(re.search(r'(?P<present>.+)\s–\s((?P<past>.+)\s–\s(?P<past_participle>.+)\s(?P<mean>.+))',_,flags=re.I))
            # print("present:{},past:{},past_participle:{}".format(_.group("present"),_.group("past"),_.group("past_participle"),_.group("mean")))
            random_list = random.sample(range(0, len(relist)), len(relist))
        for i in random_list:
            print('----------------------game start-----------------------------')
            print("present is {}".format(relist[i].group('present').lower()))
            past = input("input past:")
            print(past)
            if past.lower() == relist[i].group('past').lower():
                print("you are right")
            else:
                print("sorry,you die")
                print("present:{},past:{},past_participle:{},mean:{}".format(relist[i].group("present").lower(),relist[i].group("past"),relist[i].group("past_participle"),relist[i].group("mean")))
                continue
            past_participle = input("input past_participle:")
            print(past_participle)
            if past_participle.lower() == relist[i].group('past_participle').lower():
                print('you are right')
            else:
                print('sorry,you die')
                print("present:{},past:{},past_participle:{},mean:{}".format(relist[i].group("present").lower(), relist[i].group("past"),
                                                                     relist[i].group("past_participle"), relist[i].group("mean")))
                continue
            self.score += 1
        print("game over,total:{},you are right:{}".format(len(relist), self.score))

    # 练习模式
    def train_game(self):
            print("---------------this is train_game-----------------------")
            relist = []
            with open('buguize.txt', encoding='utf-8') as f:
                str_list = f.readlines()
            for _ in str_list:
                # print(re.search('.*\s–',_,flags=re.I).group(0))
                relist.append(
                    re.search(r'(?P<present>.+)\s–\s((?P<past>.+)\s–\s(?P<past_participle>.+)\s(?P<mean>.+))', _,
                              flags=re.I))
            # print("present:{},past:{},past_participle:{}".format(_.group("present"),_.group("past"),_.group("past_participle"),_.group("mean")))
            # 生成单词个数的随机数
            random_list = random.sample(range(0, len(relist)), len(relist))
            print(random_list)
            print('----------------------game start-----------------------------')
            # 返回错误列表
            mistake = self._train_run(random_list, relist)
            for _ in range(100):
                if mistake:
                    random_list = random.sample(range(0, len(mistake)), len(mistake))
                    mistake = self._train_run(random_list, mistake)
                else:
                    break

            print("game over,total:{},you are right:{}".format(len(relist), self.score))


if __name__ == '__main__':
    game = EngGame()
    game.train_game()