# -*- coding: utf-8 -*-
#编写一个程序，要求用户输入一个整数，然后输出两个整数root和pwr，
#满足0 < pwr < 6，并且root**pwr等于用户输入的整数。
#如果不存在这样一对整数，则输出一条消息进行说明

s = '1.23, 2.4, 3.123'
sum = 0
temp = ''
count = 0
for c in s:
    count = count + 1
    print(str(count) + ", " + str(len(s)) + ", " + c)
    if c != ',':
        temp = temp + c       
    elif c == ',' or count == len(s):        
        sum = sum + float(temp)
        temp = ''

print("和为：" + str(sum))

