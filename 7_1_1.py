def sumDigits(s):
    """ 假设s是一个字符串，返回s中十进制数字之和
        例如，如果s是'a2b3c'，则返回5
    """
    sum = 0
    for n in s:
        try:
       # if n.isdigit():
            sum += int(n)
        except ValueError:
            pass
    return sum

def sumDigitsTest():
    inputStr = input('Please input string: ')
    sum = sumDigits(inputStr)
    print('The number\'s sum is', sum)

sumDigitsTest()