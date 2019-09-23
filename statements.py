#! /usr/bin/python
# -*- coding: UTF-8 -*-

# while 第一次循环
# count = 0
# name = 'hyf'
# while (count < 9):
#     print 'The count is:', count , name
#     count = count + 1
#
# print "Good bye!"

# while 第二次循环

# i = 1
# while i < 10:
#     i += 1
#     if i % 2 > 0:
#         continue
#     print(i)
#
#
# i = 1
# while i:
#     print i
#     i += 1
#     if i > 10:
#         break

# while 第三次循环

# i = 0
# while  i < 5:
#     print i,'less than 5'
#     i += 1
# else:
#     print i,"not less tahn 5"

#for 循环第一次

# for letter  in 'Python':
#     print '当前字母 ：', letter

# for 循环第二次
# fruits = ['banana', 'apple',  'mango']
# for index in range(len(fruits)):
#     print fruits[index]

# for 循环第三次

for num in range(10,20):
    for i in range(2,num):
        if num % 2 == 0:
            j = num / i
            print '%d 等于 %d * %d' % (num, i, j)
            break
    else:
        print num, '是一个质数'