# -*- coding: utf-8 -*-
def findRoot(x, power, epsilon):
    """ x和epsilon是整数或者浮点数，power是整数
            epsilon>0 且 power>=1
        如果y**power和x的差小于epsilon，就返回浮点数y，
            否则返回None
    """
    if x < 0 and power%2 == 0:
        return None
    low = min(-1.0, x)
    high = max(1.0, x)
    ans = (high + low)/2.0
    while abs(ans**power -x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    return ans

def testFindRoot():
    epsilon = 0.0001
    for x in [0.25, -0.25, 2, -2, 8, -8]:
        for power in range(1, 4):
            print('Testing x =', str(x), 'and power =', power)
            result = findRoot(x, power, epsilon)
            if result == None:
                print('    No root')
            else:
                print('    ', result**power, '~=', x)

testFindRoot()