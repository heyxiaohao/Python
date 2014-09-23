#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 简单文件及不重要数据 序列化和反序列化模块 cPickle 或 pickle
try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(name = 'Bob', age = 20, score = 80)
print d
s = pickle.dumps(d)
print s
with open('dump.txt', 'w') as f:
    f.write(s)

with open('dump.txt', 'r') as fread:
    rs = fread.read()
rd = pickle.loads(rs)
print rd

with open('dump.txt', 'r') as fread:
    print pickle.load(fread)

# 重要数据 使用 JSON 模块 保存，也适用于不同 语言的传递
print '---------------'
import json
d = dict(name = 'Wangh', age = 20, score = 80)
json_str = json.dumps(d)
print json_str

json_d = json.loads(json_str)
print json_d
# 注：反序列化得到的字符串是unicode 需要转换 为str

# 将类序列化需要 自己编写默认序列化函数
class A(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def serial(self):
        return {
                'name' : self.name,
                'age' : self.age
                }
        
a = A('kongl', 24)
json_str = json.dumps(a, default=A.serial)
print json_str
print json.dumps(a, default = lambda obj : obj.__dict__) # 推荐此种方式，则不需要定义函数，但要排除 __slots__ 的class

def dict2obj(d):
    return A(d['name'], d['age'])

b = json.loads(json_str, object_hook = dict2obj)
print b.name
print b.age












