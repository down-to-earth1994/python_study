#!/usr/bin/python3

# 数字(Number)类型
    # python 有四种类型： 整型、布尔类型、浮点和复数
    # int
    # Bool
    # float
    # compile


# 字符串（String）
    #  python中的单引号和双引号使用完全相同
    #  使用三引号可以指定一个多行字符串
    #  转义符 '\'
    # 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
    # 字符串可以用 + 运算符连接在一起，用 * 运算符重复
    # Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始
    # Python中的字符串不能改变
    # Python 没有单独的字符类型，一个字符就是长度为 1 的字符串
    # 字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
from parser import suite
import sys
str = 'Runoob'
print(str)         # Runoob
print(str[0:1])    # Ru
print(str[0])      # R
print(str[2:5])    # noob
print(str * 2)     # RunoobRunoob
print(str + '你好') # Runoob你好
print("------------------------")
print('hello\nrunoob')
print(r'hello\nrunoob')


#等待用户输入
# input("\n\n按下 enter 键后退出。")

#同一行
# 显示多条语句
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# 多个语句构成代码组


# import 与 from...import
# 在 python 用 import 或者 from...import 来导入相应的模块。
#
# 将整个模块(somemodule)导入，格式为： import somemodule
#
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
#
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
#
# 将某个模块中的全部函数导入，格式为： from somemodule import *

for i in sys.argv:
    print(i)
print('\n python路径为', sys.path)