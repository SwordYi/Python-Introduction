# -*- coding: utf-8 -*-
#编写一个程序，要求用户输入一个整数，然后输出两个整数root和pwr，
#满足0 < pwr < 6，并且root**pwr等于用户输入的整数。
#如果不存在这样一对整数，则输出一条消息进行说明

inputStr = input("请输入整数值：")
root, pwr = 0, 2
if inputStr.isdigit():
    inputInt = int(inputStr)
    if inputInt > 0:
        while pwr < 6:
            while root < inputInt:
                root = root + 1
                print(root)
                if root**pwr == inputInt:
                    break;
                elif root**pwr > inputInt:
                    root = 0;
                    break;                
                    
            if root**pwr == inputInt:
                break;
            pwr = pwr + 1 
   
if root == 0:
    print("没有符合条件的数")
else:
    print("如何条件的root：" + str(root) + ", pwr：" + str(pwr))
    print(str(root) + "**" + str(pwr) + " = " + inputStr)

