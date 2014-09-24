#!/usr/bin/env python
# -*- coding: utf-8 -*-

# os 模块封装了 fock() 函数，但只适用于Unix/Mac 系统，且只能是Linux版的 Python 才有os.fork()函数

import os

if os.name == 'posix':
    print 'Process (%s) start...' % os.getpid()
    pid = os.fork()
    if pid == 0: # 子进程
        print "I'm child process (%s) and my parent is (%s)" % (os.getpid(), os.getppid())
    else:
        print 'I (%s) just create a child process (%s)' % (os.getpid(), pid)

# 跨平台的 多进程模块 multiprocessing
from multiprocessing import Process
import os

#子进程要执行的代码
def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__ == '__main__':
    print 'Parent process %s' % os.getpid()
    #创建进程
    p = Process(target = run_proc, args = ('test',))
    print 'Process will start'
    p.start()
    p.join() # 等待子进程的结束
    print 'Process end'
    
# 进程池
#进程池的大小，默认等于处理器的 核心数，可改变 p = pool(5)
from multiprocessing import Pool
import os, random, time

def long_time_task(name):
    print 'Run task %s (%s)' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds' % (name, (end - start))
    
if __name__ == '__main__':
    print 'Parent process %s' % os.getpid()
    p = Pool(9)
    for i in range(5):
        p.apply_async(long_time_task, args = (i,))
    print 'Wait for all subprocess done...'
    p.close() # close 后进不能在加入process
    p.join()
    print 'All subprocess end...'
    
# 进程间通讯 Queue 或 Pipes
from multiprocessing import Process, Queue
import os, random, time

def write(q):
    for value in ['a', 'b', 'c']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(4)

def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue...' % value
        
if __name__ == '__main__':
    # 父进程创建queue，并传给子进程
    q = Queue()
    pw = Process(target = write, args = (q,))
    pr = Process(target = read, args = (q,))
    # 启动写进程
    pw.start()
    # 启动读进程
    pr.start()
    # 等待结束
    pw.join()
    # 死循环强行结束
    pr.terminate()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    