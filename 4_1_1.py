# -*- coding: utf-8 -*-
# 编写一个函数isIn，接受两个字符串作为参数，
# 如果一个字符串是另一个字符串的一部分，返回True，否则返回False。
# 提示：你可以使用内置的str类型的操作符in。

def isIn(smallStr, bigStr):
    if smallStr in bigStr:
        return True
    else:
        return False

print('aaa in bbbb is', isIn('aaa', 'bbbb'))
print('sgt in gtugsgtgge is', isIn('sgt', 'gtugsgtgge'))


def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName + ', ' + firstName)
    else:
        print(firstName, lastName)

printName('Olga', 'Puchmajerova', False)
printName('Olga', 'Puchmajerova', reverse = False)
printName('Olga', lastName = 'Puchmajerova', reverse = False)
printName(lastName = 'Puchmajerova', firstName = 'Olga', reverse = False)