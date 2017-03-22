import os, time, random
# print('Process (%s) start....'% os.getpid())
# pid=os.fork()
# if pid==0:
#   print('i am child process(%s) and my parent is %sjj' %(os.getpid(), os.getppid()))
# else:
#   print('i (%s) just created a child process(%s)' %(os.getpid(),pid))
from multiprocessing import Process
import time
#子进程执行的代码
# def run_proc(name):
#   print('Run child process %s (%s)....' %(name,os.getpid()))
# if __name__ =="__main__":
#   print('Parent process %s.' % os.getpid())
#   p=Process(target=run_proc,args=('test',))
#   print('Child process will start.')
#   p.start()
#   # time.sleep(5)
#   p.join()

from multiprocessing import Pool

# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))


# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(5)
#     for i in range(5):
#       p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()#等待子进程加入
#     print('All subprocesses done.')

# def allpoll(name):
#   print('run task %s (%s)' %(name,os.getpid()))
#   start=time.time()
#   time.sleep(random.random()*3)
#   end=time.time()
#   print('task %s runs %0.2f seconds.' % (name,(end-start)))
#
# if __name__=='__main__':
#   print('parent process %s' % os.getpid())
#   po=Pool(6)
#   for i in range(6):
#     po.apply_async(allpoll,args=(i,))
#   print('waiting for all subprocess done....')
#   po.close()
#   po.join()
#   print('all subprocess done.')
  # 很多时候子进程并不是自身，而是一个外部地址。创建子进程，还需要控制子进程的输入和输出
#subprocess模块可以让我们非常方便的启动进程，然后控制输入和输出

# import subprocess
# print('$ nslookup www.python.org')
# r=subprocess.call(['nslookup','www.python.org'])
# print('Exit code:',r)
#
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# # print(output.decode('utf-8'))
# print('Exit code:', p.returncode)

from multiprocessing import Queue

def write(q):
  print('wtite process%s' %os.getpid())
  for i in [1,2,3,4,5]:
    print('put %s queue' %i)
    q.put(i)
    time.sleep(random.random())
def read(q):
  print('read process %s' %os.getpid())
  while True:
    value=q.get(True)
    print('get %s queue' %value)
if __name__=="__main__":
  q=Queue()
  pw=Process(target=write,args=(q,))
  pr=Process(target=read,args=(q,))
  pw.start()
  pr.start()
  pw.join()
  pr.terminate()#读取时死循环，所以需要强制停止