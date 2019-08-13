def findAnEven(L):
    """ 假设L是一个整数列表，返回L中的第一个偶数
        如果L中没有偶数，则抛出ValueError异常
    """
    result = 0
    for n in L:
        if n % 2 == 0:
            result = n
            break
    if result != 0:
        return result
    else:
        raise ValueError('ValueError')


def findAnEvenTest():
    try:
        L = [2,3,4,5,6]
        print(L, '\'s first even is:', findAnEven(L))
        L = [1,3,6,5,8]
        print(L, '\'s first even is:', findAnEven(L))
        L = [1,3,7,5,8]
        print(L, '\'s first even is:', findAnEven(L))
        L = [1,3,7,5,9]
        print(L, '\'s first even is:', findAnEven(L))
    except ValueError as msg:
        print(L, '\'s first even is:', msg)

findAnEvenTest()