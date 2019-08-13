def isPal(x):
    """ 假设x是列表
        如果列表是回文，则返回True，否则返回False
    """
    temp = x[:]
    temp.reverse()
    print('temp:', temp)
    print('x:', x)
    if temp == x:
        return True
    else:
        return False

def silly(n):
    """ 假设n是正整数，接受用户的n个输入
        如果所有输入组成一个列表，则返回'Yes'，否则返回'No'
    """
    result = []
    for i in range(n):        
        elem = input('Enter element: ')
        result.append(elem)
    if isPal(result):
        print('Yes')
    else:
        print('No')

silly(2)