# coding =utf -8
# 直接赋值 完全切片 深拷贝 浅拷贝的理解
import copy

a = [1, 3, 5, 7, 10, [1, 3, ]]
# 直接赋值  实际复制的是a的地址(引用) a对象更改b对象也会更改  is是比较id是否相同 跟c好像不大一样
# print(a)
# b = a
# a .append(3)
# print(id(a))
# print(id(b))
# print(a)
# print(b)

# 完全切片
# 切片：对“是不可变对象的子元素“的修改或增删操作不会影响另一对象
# 切片：对“是可变对象的子元素“的操作会影响另一对象
# b = a[:]
# print(id(b[5]))
# print(id(a[5]))
# print(id(a))
# print(id(b))
# a[5].append(99)
# print(a)
# print(b)

# 浅拷贝 类似于完全切片
# b = copy.copy(a)
# print(id(a))
# print(id(b))
# print(id(a[5]))
# print(id(b[5]))

# 深拷贝
b = copy.deepcopy(a)
print(id(a))
print(id(b))
print(id(a[5]))
print(id(b[5]))



