#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 实现必须的函数
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello,World</h1>'

# 导入WSGI模块
from wsgiref.simple_server import make_server
# 创建一个服务器
httpd = make_server('', 8000, application)
print 'Servint HTTP on Port 8000...'
# 开启监听
httpd.serve_forever()