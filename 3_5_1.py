# -*- coding: utf-8 -*-
# 在牛顿-拉弗森法的实现中添加一些代码，跟踪求平方根所用的迭代次数。
# 在这段代码的基础上编写一个程序，比较牛顿-拉弗森法和二分查找法的效率
# （你会发现牛顿-拉弗森法效率更高）。

import datetime

epsilon = 0.01
k = 240000
guess = k/2.0
numGuesses = 0

print('----Newton algorithm----')
start_time = datetime.datetime.now()
while abs(guess**2 - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
    print('guess =', guess)
    numGuesses += 1
end_time = datetime.datetime.now()
print('numGuesses =', numGuesses)
print('Square root of', k, ' is about', guess)
newtonCostTime = end_time - start_time
print('Newton algorithm cost time is', newtonCostTime)
print()

numGuesses = 0
low = 0.0
high = max(1.0, k)
ans = (high + low) / 2.0

print('----Equinoctial algorithm----')
start_time = datetime.datetime.now()
while abs(ans**2 - k) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**2 < k:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
end_time = datetime.datetime.now()
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', k)
equinoctialCostTime = end_time - start_time
print('Equinoctial algorithm cost time is', equinoctialCostTime)
print()

print('----Compare algorithm----')
if newtonCostTime < equinoctialCostTime:
    print('Newton algorithm is faster')
elif newtonCostTime > equinoctialCostTime:
    print('Equinoctial algorithm is faster')
else:
    print('Newton algorithm is equal to Equinoctial algorithm')






