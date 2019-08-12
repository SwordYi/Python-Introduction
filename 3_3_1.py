# -*- coding: utf-8 -*-
#求立方根

res = 27
x = abs(res)
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low) / 2.0
while abs(ans**3 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print('numGuesses =', numGuesses)
if res < 0:
    ans = ans * (-1)
print(ans, 'is close to square root of', res)