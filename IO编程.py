#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

# 打开文件
try:
    f = open('a.txt', 'r') # 文件不存在，抛出IOError异常
except IOError:
    print 'can not open file'
else:
    try:
        print f.read() # 读文件失败，抛异常，需要在finally中关闭文件
    finally:
        print 'file.colse()'
        f.close()
# with as 方法帮助调用 close 方法
with open('b.txt', 'r') as ff:
    print ff.read()
# read(size) 可以每次读size个字节
# readline() 每次读取一行
# readlines() 读取所有，按行返回一个list   line.strip() 忽略末尾的 \n
# 读取方式  rb 要读取非ASCII编码的文件，必须以二进制打开，在解码，如gbk文件
with open('c.txt', 'rb') as fff:
    u = fff.read().decode('gbk')
    print u
# 读文件是自动转码模块 codecs
import codecs
with codecs.open('c.txt', 'r', 'gbk') as ffff:
    print ffff.read()
    
# 写文件
# 区别在于 w wb

# 操作文件和目录 os 模块 和 os.path 模块
import os
print os.name
print os.environ # 返回dict
print os.getenv('PATH')
# 查看当前目录绝对路径
p = os.path.abspath('.')
print os.path.abspath('.')
# 在某个路径下创建新目录
absp = os.path.join(p, 'testdir') # 首先表示决定路径  创建路径
print absp
#os.mkdir(absp) # 然后创建出目录 如果存在 抛出异常
# 删掉一个目录
#os.rmdir(absp)

# 拆分路径 
print os.path.split(absp) # 分为两部分，第二部分为最后级别及目录或文件名
print os.path.splitext('G:\eclipse\Python\a.txt') # 获取文件扩展名

# 重命名
#os.rename('f.txt', 'a.txt')

# 删除文件
#os.remove('ee.txt')

# 复制文件不在os模块 在 shutil 模块中
import shutil
shutil.copyfile('a.txt', 'm.txt')

# 列出当前目录所有目录
print [x for x in os.listdir('.') if os.path.isdir(x)]

# 列出所有.py文件
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']





















