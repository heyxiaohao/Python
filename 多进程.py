#!/usr/bin/env python
# -*- coding: utf-8 -*-

# os 模块封装了 fock() 函数，但只适用于Unix/Mac 系统，且只能是Linux版的 Python 才有os.fork()函数
'''
import os

print 'Process (%s) start...' % os.getpid()
pid = os.fork()
if pid == 0: # 子进程
    print "I'm child process (%s) and my parent is (%s)" % (os.getpid(), os.getppid())
else:
    print 'I (%s) just create a child process (%s)' % (os.getpid(), pid)
'''

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