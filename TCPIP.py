#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading, time

type = 'clident'
if type == 'client':
    # 创建socket AF_INET IPV4  AF_INET6 IPV6
    address = ('127.0.0.1', 9999)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    s.connect(address)
    # 接收欢迎消息:
    print s.recv(1024)
    for data in ['Michael', 'Tracy', 'Sarah']:
        # 发送数据:
        s.send(data)
        print s.recv(1024)
        s.send('exit')
    s.close()
   
else:
    def tcplink(sock, addr):
        print 'Accept new connect from %s:%s...' % addr
        sock.send('Welcome')
        while True:
            data = sock.recv(1024)
            time.sleep(5)
            if data == 'exit' or not data:
                break
            sock.send('Hello %s' % data)
        sock.close()
        print 'Connection from %s:%s closed' % addr
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 监听端口
    s.bind(('0.0.0.0', 9999))
    s.listen(5)
    print 'waiting for connect...'
    while True:
        # 接收一个新连接
        sock, addr = s.accept()
        # 创建新线程处理
        t = threading.Thread(target = tcplink, args = (sock, addr))
        t.start()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        