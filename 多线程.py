#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 低级模块 thread 高级模块 threading(常用)
import threading, time

# 线程执行代码
def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n += 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s end' % threading.current_thread().name
    
if __name__ == '__main__':
    print 'thread %s is running...' % threading.current_thread().name
    t = threading.Thread(target = loop, name = 'LoopThread')
    t.start()
    t.join()
    print 'thread %s end' % threading.current_thread().name

# 锁 lock = threading.Lock()  lock.acquire()  lock.release

# ThreadLocal 解决不同线程处理同一个对象时  免去 传参 及 全局变量的方式、  常用于：每个线程绑定一个数据库连接，HTTP请求，用户身份信息等
# 创建全局ThreadLocal对象 
local_school = threading.local()

def process_student():
    print 'Hello %s (in %s)' % (local_school.student, threading.current_thread().name)

def process_thread(name):
    # 绑定TrheadLocal的student
    local_school.student = name
    process_student()

t1 = threading.Thread(target = process_thread, args = ('wangh',), name = 'ThreadA')
t2 = threading.Thread(target = process_thread, args = ('kongl',), name = 'ThreadB')
t1.start()
t2.start()
t1.join()
t2.join()














