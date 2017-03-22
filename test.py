# def is_odd(n):
#     return n%2==1
# fi=list(filter(is_odd,[1,2,4,5,6,9,10,15]))
# print('保留奇数',fi)
# def not_empty(s):
#     return s and s.strip()
# em=list(filter(not_empty,['A','','B',None,'C',' ']))
# print(em)
#
#
# print('排序')
#
# print(sorted([36,-12,23,2,34],key=abs))
#
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(t):
#     return t[0]
#
# L1=sorted(L,key=by_name)
# print(L1)
#
# def by_score(t):
#     return t[1]
# L2=sorted(L,key=by_score)
# print(L2)
#
# print('返回函数')
#
# def calc_sum(*args):
#     ax=0
#     for n in args:
#         ax=ax+n
#     return ax
#
# def lany_sun(*args):
#     def sum():
#         ax=0
#         for n in args:
#             ax=ax+n
#         return ax
#     return sum
# f=lany_sun(1,2,3,4,5)
# print(f())
#
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
#
# f1, f2, f3 = count()
# print(f1(),'-',f2 (),'-',f3())
#
# def count1():
#     def f(j):
#         # def g():
#         #     return j*j
#         # return g
#         return lambda :j*j
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
#     return fs
# f3,f4,f5=count1()
# print(f3(),'-',f4 (),'-',f5())
#
#
# f=lambda x:x*x
# print(f(5))
#
# test1=lambda x,y:x**y#幂函数
# print(test1(2,4))
#
# print('装饰器')
# def now():
#     print('2017-03-11')
# f=now
# f()
#
# print(now.__name__)
# print(f.__name__)
#
# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
# @log#@log等价于now=log(now)
# def now1():
#     print('2017-03-11')
#
# now1()
#
# def log1(text):
#     def decorator(func):
#         def wrapper(*args,**kw):
#             print('%s %s():' % (text,func.__name__))
#             return func(*args,**kw)
#         return wrapper
#     return decorator
#
# @log1('test')
# def now3():
#     print('test')
# now3()
#
# # 完整的装饰器
#
# import functools
# def log4(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kw):
#         print('call %s():' % func.__name__)
#         return func(*args,**kw)
#     return wrapper
#
# # 偏函数
# int2=functools.partial(int,base=2)
#
# print(int2('1000'))
#
# # 使用模块 2017-03-11 1:14:00
# import time
# print(time.ctime())
# print(time.localtime())
# print(time.timezone)
# __author__='amos'
# import sys
# print(sys.argv)#当前执行的文件路径
# print(__name__)
#
#

# print('*'*10)
# for i in range(5):
#     print("         *")
# print('*'*10)
# for i in range(5):
#     print("         *")
# print('*'*10)
#
# import logging
# logging.basicConfig(level=logging.INFO)
# s = '3'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)
#调试
# import pdb
# aa='3'
# a1=int(aa)
# pdb.set_trace();
# print(10 / a1)
# 文件读写  读取文件用r,读取图片、视频等二进制流用rb
f=open('test.txt','r')
print(f.read())
f.close()
print("-----------with open() as f:--------")
with open('test.txt','r') as f:
    print(f.read())
#位置参数 关键字参数
ll=[1,2,3,4,5]
print(ll)
print('----------------')
for ss in ll:
    print(ss)
for i in range(10):
    print(i)
print('-----------------读取视频------------------')
with open('ss.jpg','rb') as m:
    print('十六进制表示的字节：',m.read())
# 读取非utf-8编码的文本需要给open（）传入第三个参数encoding='gbk';open('test.txt','r',encoding='gbk')
# 遇到有些编码不规范的文件，你可能会与遇到UnicodeDecodeError,因为在文本中可能夹杂了一些非法编码的字符。
# 可以给open()传入errors='ingore'直接忽略掉 open('','',encoding='gbk',errors='ingore')

print('----------------写文件-----------------------')
# w或wb
with open('test.txt','w') as f1:
    f1.write('xsd amos')
with open('test.txt','r') as f2:
    print(f2.read())

import os

ll=[d for d in os.listdir('./')]
print(ll)

aa={'a':1,'b':2}

for k in aa.keys():
    print('key=',k)
for v in aa.values():
    print('values=',v)
for k,v in aa.items():
    print('key =',k,'values=',v)
print(aa)
# print(os.getcwd())
# os.chdir('d:');
try:
  print(os.getcwd())
finally:
    print('finally')
# StringIO 内存中读写str(只能是str)
from io import StringIO
f=StringIO()
f.write('hello')

print('stringio:',f.getvalue())
# getvalue() 方法获取写入后的str 也可以对StringIO做初始化StringIO('test')
# BytesIO 实现了内存中读写bytes
from io import BytesIO
b=BytesIO()
b.write('中文'.encode('utf-8'))
print(b.getvalue())
# 写入的是经过utf-8编码的bytes

print('操作系统类型：',os.name)
# nt 是windows posix是linux uninx或mac os x

# print('系统详细信息：',os.uname())
# windows 下不支持uname()
print('环境变量：',os.environ)
print('获取单个指定的环境变量：',os.environ.get('APPDATA'))

print('----------操作文件和目录------------------------')
abspath=os.path.abspath('.')
print(abspath)#查看当前目录的绝对路径
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
os.path.join('E:/webwork/python','testdir')
# os.mkdir('E:/webwork/python/testdir')#然后创建一个目录：
# os.rmdir('E:/webwork/python/testdir')#删除一个目录
# os.rename('test.txt1','test.txt')#文件重命名
# os.remove(name)#删除文件
# import shutil
# shutil.copyfile('e:/webwork/python/test.txt','e:/webwork/python/testdir/')
gg=os.path.isdir('testdir')
print(gg)

alldir=[dd for dd in os.listdir('.') if os.path.isdir(dd)]
print(alldir)

allpyfile=[ff for ff in os.listdir('.') if os.path.isfile(ff) and os.path.splitext(ff)[1]=='.py']
print(allpyfile)