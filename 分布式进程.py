#!/usr/bin/env python
# -*- coding: utf-8 -*-
import multiprocessing

# multiprocessing 的 子模块 managers 将网络通讯封装，可以静默升级 在同一台机器上的 多进程程序，如 只需要将 Queue 通过managers暴露在网上即可

type = 'd'
if type == 'server':
    # 服务器端，负责创建Queue，发布到网络，并向其中写任务，但是分布式的 Queue不能直接拿到，需要通过manager.get_task_queue()获得Queue
    # 在windows 上跑不了 服务端
    import random, time, Queue
    from multiprocessing.managers import BaseManager
    
    # 发送任务的队列
    task_queue = Queue.Queue()
    # 接收结果的队列
    result_queue = Queue.Queue()
    
    # 从BaseManager 继承的QueueManager
    class QueueManager(BaseManager):
        pass
    
    # 把两个queue注册到网络
    QueueManager.register('get_task_queue', callable = lambda : task_queue)
    QueueManager.register('get_result_queue', callable = lambda : result_queue)
    # 绑定端口5000，验证码'abc'
    manager = QueueManager(address = ('', 5000), authkey = 'abc')
    # 启动queue
    manager.start()
    # 获得通过网络访问的Queue的对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 放入任务
    for i in range(10):
        n = i #random.randint(0, 10000)
        print 'Put task %d...' % n
        task.put(n)
    # 从result读取结果
    print 'Try get results...'
    for i in range(10):
        r = result.get(timeout = 10)
        print 'Result: %s' % r
    # 关闭
    manager.shutdown()

else:
    # 客户端
    import time, sys, Queue
    from multiprocessing.managers import BaseManager
    
    # 创建雷类似的QueueManager
    class QueueManager(BaseManager):
        pass
    # 由于这个QueueManager只能从网络拿到，所以注册是提供名字
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')
    # 连接到服务器
    server_addr = '192.168.1.108'
    print 'Connect to server %s...' % server_addr
    # 端口和验证码要正确
    m = QueueManager(address = (server_addr, 5000), authkey = 'abc')
    # 从网络连接
    m.connect()
    # 获取Queue对象
    task = m.get_task_queue()
    result = m.get_result_queue()
    # 从task去除任务，处理并返回结果
    for i in range(10):
        try:
            n = task.get(timeout = 5)
            print 'run task %d * %d...' % (n, n)
            r = '%d * %d = %d' % (n, n, n * n)
            time.sleep(1)
            result.put(r)
        except Queue.Empty:
            print 'task queue is empty'
    #处理结束
    print 'exit'
    















 