# import time;
# str='i love you';
# print(str);
# print(str[3]);
# print(str[3:6]);
# list=['a','b','c'];
# list[1]=4;
# print(list);
# tuple=(1,2,3,4);
# # tuple[1]='b';//元组是不允许更新的
# print(tuple);
# # 元字典dict={};
# dict={"name":123};
# dict['sex']=1;
# print(dict);
# print(time.time());
# print(time.localtime(time.time()));

# def person(name,age,*,city='shanghai',job):
#     print('name:',name,'age:',age,'other',city,job)
# person('amos',23,job='php')

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

res=fact(3)
print(res)

def move(n,a,b,c):
    if n == 1:
        print(a, '->', c)
        return
    move(n - 1, a, c, b)
    move(1, a, b, c)
    move(n - 1, b, a, c)
move(3,'A','B','C')

L=['amos','alice','diamond','red','blur']
r=[]
for i in range(3):
    r.append(L[i])
print(r)
# 切片
print('切片',L[0:3])
L1=list(range(100))
print(L1[-6:])
print('切片前10个中每两个取一个',L1[:10:2])

str1='amos'
print(str1[-2:])


# 迭代
print('-----------迭代---------')
dic1={'a':1,'b':2,'c':3,'d':4}
print(dic1)

for key in dic1:
    print('key:',key)
for value in dic1.values():
    print('value:',value)
for key,value in dic1.items():
    print('all:',key,'=>',value)
# 判断是否可以迭代
from collections import Iterable
is1=isinstance(1123,Iterable)
print(is1)

for i,v in enumerate(dic1):
    print(i,v)
lis=list(range(1,10))
print(lis)
lis2=[x*x for x in range(1,10) if x%2==0]
print(lis2)

#列出目录和文件名
import os
dir=[d for d in os.listdir('../../')]
print('当前目录所有文件和目录',dir)
LL=['HELLO','TEST',12]
ll=[s.lower() for s in LL if(isinstance(s,str)==True)]
print('大写',LL)
print('小写',ll)

g=(x*x for x in range(1,10))
print(next(g))
print(next(g))

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
# for n in fib(5):
#     print(n)
#
# def triangles():
#     L = [1]
#     while True:
#         yield L
#         L.append(0)
#         L = [L[i - 1] + L[i] for i in range(len(L))]
# n1 = 0
# for n in triangles():
#     if n1<10:
#      # print(n)
#      n1=n1+1
#
# def f(n):
#     return n*n

# f1=map(f,[1,2,3,4,5])
# print(list(f1))

print('类和实例')
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print('%s :%s' % (self.name,self.score))

Student.name='amos'
print(Student.name)