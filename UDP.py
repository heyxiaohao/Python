#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

address = ('127.0.0.1', 9999)

type = 'serdver'
if type == 'server':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(address)
    print 'Bind UDP on 9999...'
    while True:
        data, addr = s.recvfrom(1024)
        print 'Receive from %s:%s' % addr
        s.sendto('Hello %s' % data, addr)
        
else:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for data in ['wangh', 'kongl', 'yee']:
        s.sendto(data, address)
        print s.recv(1024)
    s.close()