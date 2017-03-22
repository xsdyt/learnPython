#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__='amos'
__title__='practice'
__date__='2017-03-11 09:26:34'

# 1.
a=2
b=3
print(a+b)
# 2.
L=[2,9,3,6]
L=sorted(L)
print(list(L))
#or
L=[2,9,3,6]
L.sort()
print(L)

def foo():
    print('try 123')
try:
    foo()
except ZeroDivisionError as e:
    print('error',e)
finally:
    print("finally")


