# -*- coding: utf-8 -*-
#编写一个程序，检查3个变量x、y和z，输出其中最大的奇数。如果其中没有奇数，就输出一个消息进行说明

roop = 10
maxJiShu = 0
while roop > 0:
    roop = roop -1
    inputStr = input("请输入整数值：")
    if inputStr.isdigit():
        inputInt = int(inputStr)
        if inputInt % 2 != 0:
            if maxJiShu == 0:
                maxJiShu = inputInt
            elif maxJiShu < inputInt:
                maxJiShu = inputInt
    
if maxJiShu == 0:
    print("没有输入任何奇数")
else:
    print("最大的奇数是：" + str(maxJiShu))

