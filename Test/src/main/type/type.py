#!/usr/bin/python3
counter = 100  # 整型变量
miles = 100  # 浮点变量
name = "runoob"  # 字符串

print(counter)
print(miles)
print(name)

# 多个变量赋值
# a = b = c = 1
# a,b,c = 1,2,"runoob"

# 标准数据类型
# Number String List Tuple Set  Dictionary
# python3 六个标注啊数据类型
# 不可变数据(3 个) Number(数字)、String(字符串)、Tuple(元组)
# 可变数据（3 个）List(列表) Dictionary（字典） Set（集合）

# Number
# Python3 支持 int、float、bool、complex（复数）
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))

# isinstance 和 type 的区别在于：

# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。

print(5 + 4)
print(4.3 - 2)
print(3 * 7)
print(2 / 4)
print(2 // 4)
print(17 % 3)
print(2 ** 5)

# String (字符串)


# List(列表)

list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']
print(list)
print(list[0])  # 输出列表的第一个元素
print(list[1:3])  # 输出列表从第二个到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表


def reverseWords(input):
    inputWords = input.split(" ")
    inputWords = inputWords[-1::-1]
    output = ' '.join(inputWords)
    return output

rw = reverseWords('I like runoob')
print(rw)

#Tuple(元组)

tuple = ('abcd',786,2.23,'runoob',70.2)
tinytuple = (123,'runoob')
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple * 2)
print(tuple + tinytuple)

# 虽然tuple 不可变 但是可以包含可变的对象 比如list 列表
tup1 = () # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
# String,list 和 tuple 都属于sequence (序列)

# Set(集合)
# 可以使用大括号{} 或者 set() 函数创建集合
# 创建空集合必须使用set() 而不是{} 因为{ } 是来创建一个空字典
# 创建格式
student= {'Tom','Jim','Mary','Tom','Jack',"Rose"}
print(student) #  输出集合元素被自动过滤掉了

#成员测试
if 'Rose' in student :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')

#Set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b) # a 和 b 的差集
print(a | b) # a 和 b 的并集
print(a & b) # a 和 b 的并集
print(a ^ b) # a 和 b 不同时存在的元素

#Dictionary(字典)
dict={}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"
tinydict = {'name':'runoob','code':1,'site':"www.runoob.com"}
print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

#dict
# hyf=dict([('Runoob',1),('Google',2),('Taobao',3)]) # 字典中创建list 并不是按照创建的顺序输出
# print(hyf)
#
# hyf1={x: x**2 for x in(2,4,6)}
# print(hyf1)

#字典是一种映射类型，它的元素是键值对
#字典关键字必须为不可变类型，且不能恢复
#创建空字典使用{}



# Python 数据类型转换
# int(x) 将 x 转换为一个整数类型
# float(x) 将 x 转换到一个浮点数
# complex() 创建一个复数
# str() 将对象 x 转换为字符串
# repr(x) 将对象 x 转换为表达式字符串
# eval(str) 用来计算在字符串中的有效Python 表达式，并返回一个对象
# tuple(s) 将序列 s 转换为一个元组
# list(s)  将序列 s 转换为一个列表
# set(s)   转换为可变集合
# dict(d)  创建一个字典，d必须是一个（key，value）元组序列
# frozenset(s) 转换为 不可变集合
# chr(x) 将一个整数转换为一个字符串
# ord(x) 将一个整数转为一个16进制字符串
# hex(x) 将一个整数转为一个16进制字符串
# oct(x) 将一个整数转为一个八进制字符串