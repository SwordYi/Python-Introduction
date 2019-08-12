# -*- coding: utf-8 -*-
count = 0
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        if n == 2:
            global count
            count = count + 1
        return fib(n-1) + fib(n-2)
def testFib(n):    
    print('fib of', n, '=', fib(n))
    print('call 2\'s count =', count)

testFib(5)