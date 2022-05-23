# coding = utf-8
# 字典
p_dict = {"hps": "100", 'acs': "30", "sbs": "99", "bbs": "33"}
del p_dict["hps"]
print(p_dict)

# 指定键不存在时利用p_dict["hp"]访问会出错 故用get方法
print(p_dict.get("hps"))

# 遍历字典 直接遍历遍历的是键
for key in p_dict:
    print(key)
# 等同于
for key in p_dict.keys():
    print(key)
# for key, value, d in p_dict:
#     print(d)
#     print("key:\t{}\t".format(key), end='')
#     print("value:\t{}\t".format(value))

for key, value in p_dict.items():
    print("key:\t{}\t".format(key), end='')
    print("value:\t{}\t".format(value))

# 按特定顺序遍历键
for key in sorted(p_dict.keys()):
    print(key)

for value in p_dict.values():
    print("遍历值: {}".format(value))

    # 这种做法取字典中的值没有考虑是否重复。涉及的值很
    # 少时，这也许不是问题，但如果被调查者很多，最终的列表可能包
    # 含大量重复项。为剔除重复项，可使用集合（set）。集合
    # 中的每
    # 个元素都必须是独一无二的：

# 嵌套
# 批量生成外星人
alien_wares = []
alien_ware = {"color": "green", "points": 5, "speed": "slow"}
for i in range(30):
    alien_wares.append(alien_ware)
print(alien_wares[5:10])
print(len(alien_wares))

# 字典中存储列表
favorite_languages = {
    'jen': ['python进阶', 'ruby'],
    'sarah': ['c'],
    "he": ["java"]
}
for key, value in favorite_languages.items():
    print("key:{}".format(key.title()), end='')
    for book in value:
        print("  book is {}".format(book.title()), end='')
    print("")


# 字典中存储字典
users = {
    'aeinstein':{
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
    },
    'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
    },
}

for user, user_info in users.items():
    print(user)
    print(user_info)


# 集合 无序 无重复
jihe = {"java", "python进阶", "c++", "java"}





