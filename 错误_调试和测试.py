#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 错误处理机制 try  except  finally
print '-----错误处理-----'

try:
    r = 10 / 1
    print 'try...'
except ZeroDivisionError, e:
    print e
else: # else 语句块 在没有错误时执行
    print 'else...'
finally:
    print 'finally...'
print 'End'  

# 错误基类 BaseException

print '使用内置logging模块打印错误信息'
import logging
logging.basicConfig(level=logging.INFO)

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        print e
        logging.exception(e) # 可以打印出堆栈信息
main()
print 'End'

# 抛出错误 raise 可以抛出错误对象，也可以单独使用 raise 用于将错误抛出，供上层处理
def func1(s):
    return 10 / int(s)
def func2(s):
    try:
        func1(s)
    except ZeroDivisionError:
        print 'Error'
        raise

def main():
    try:
        func2('0')
    except ZeroDivisionError, e:
        logging.exception(e)
main()
print '---------------'

print '-----调试-----'
# 使用 print
# 使用断言， -O 参数关闭断言
try:
    n = 0
    assert (n != 0) # 抛出AssertError异常
except AssertionError, e:
    logging.exception(e)
else:
    10 / n
# 使用logging模块
print '---------------'
# import logging 
# logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print 10 / n
    
print '-------------'



























