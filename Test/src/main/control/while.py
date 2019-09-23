#!/usr/bin/python3
# a,b  = 0,1
# while b < 10:
#     print(b)
#     a,b = b, a+b

a,b = 0,1
while b<1000:
    print(b,end=",")
    a,b = b, a+b

def fab(n):
    if n < 1:
        print("输入有误！")
        return  - 1
    if n == 1 or n ==2:
        return 1
    else:
        return fab(n-1) + fab(n-2)
#斐波纳契 数字
result=fab(10)
print(result)

# var = 1
# while var == 1:
#     num = int(input("请输入一个数字 :"))
#     print("你输入的数字是:",num)
# print("Good bye!")


sites = ["Baidu","Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程")
        break
    print("循环数据" + site)
else:
    print("没有循环数据!")
print("完成循环!")

# for i in range(5):
#     print(i)

# list = [1,2,3,4]
# it = iter(list)
# for x in it:
#     print(x,end=" ")
import sys
list = [1,2,3,4]
it = iter(list)
while True:
    try:
        print(next(it))
    except StopAsyncIteration:
        sys.exit()