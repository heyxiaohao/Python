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

# ThreadLocal 解决不同线程处理同一个对象时  免去 传参 及 全局变量的方式

