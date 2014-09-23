#!/usr/bin/env python
# -*- coding: utf-8 -*-
from _ast import Num

class Student(object): # object 是所有对象的基类
    def __init__(self, name, score, id): # 构造函数
        self.name = name
        self.score = score
        self.__id = id # 成员变量前加 __ 表示私有变量，无法从外部访问

    def print_score(self):
        print '%s, %s' % (self.name, self.score)
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.id = id
        
bart = Student('Bart', 95.0, 1) # 实例化类
list = Student('List', 87.1, 2)
bart.print_score() # 成员函数调用
list.print_score()
bart.sex = '女' # 可以动态的添加属性，但是只对当前对象有效
print bart.sex
# print list.sex # 抛出异常AttributeError

print bart.name
#print bart.__id # 抛出异常AttributeError
print bart.id

class Animal(object):
    def run(self):
        print 'Animal is running...'

class Dog(Animal):
    def run(self): # 覆盖父类方法
        print 'Dog is running...'

    def __len__(self): # 要获取自定义类型的len方法  需要自己编写 __len__()函数
        return 3

class Cat(Animal):
    def run(self):
        print 'Cat is running...'

class Tortoise(Animal):
    def run(self):
        print 'Tortoise is running...'

dog = Dog()
cat = Cat()
dog.run()
cat.run()

def run_(animal):
    animal.run()

run_(Dog())
run_(Cat())
run_(Tortoise())


# 获取对象信息
print '---获取对象信息---'
print type(123)
print type('abc')
print type([])
print type(str)
print type(Animal)
print type(dog)

# 每一种内置类型都在 types 模块有定义
import types
print type(123) == types.IntType
print type(Animal) == types.TypeType

# 判断类型 isinstance()
print '---isinatance()---'
print isinstance(dog, Animal)
print isinstance(dog, (Dog, Animal)) # 可以判断是否是中的一种类型

# 获取对象的所有属性和方法
print '---dir()---'
print dir(dog)

print len(dog)

# getattr() setattr() hasattr()
try:
    print hasattr(bart, name)
except NameError:
    pass

# 可以动态的给对象绑定属性
class A(object):
    pass
print '---动态绑定属性---'
a = A()
b = A()
a.name = 'abc' # 仅对当前对象有效
print a.name
try:
    print b.name
except AttributeError:
    pass
print '---动态绑定方法---'
def set_age(self, age): # 定义方法体
    self.age = age
from types import MethodType # 导入模块方法
a.set_age = MethodType(set_age, a, A) # 此方式只对当前实例有效
a.set_age(24)
print a.age

# 对所有实例都有效的动态绑定方法的方式 给类绑定
def set_score(self, score):
    self.score = score
A.set_score = MethodType(set_score, None, A)
b.set_score(54)
print b.score

# 限制动态创建属性  __slots__ 变量 只对当前类有效，对子类无效
print '---限制---'
class B(object):
    __slots__ = ('name', 'age')
c = B()
c.name = 'ad'
c.age = 12
try:
    c.score = 'adf'
except AttributeError:
    print 'AttributeError'

# @property 装饰器  将方法变为属性，可通过直接属性调用，并可检测参数值
print '---@property---'
class C(object):
    def __init__(self):
        self.__score = 10
        
    def __len__(self):
        return 9
    
    @property # 只定义它，就只有getter
    def score(self):
        return self.__score
 
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer!')
        if value < 0 or value > 100:
            raise ValueError('score must be between 0 ~ 100')
        self.__score = value

cc = C()
cc.score = 60
print cc.score
try:
    cc.score = 9999
    print cc.score
except ValueError:
    print 'ValueError'

print len(cc)
    
# Python 支持多重继承

# 类 内置属性
print '类内置属性'
# __repr__ 打印实例的地址，但是对于用户而言无用，因此自定义__str__方法，让__repr__ = __str__
class D(object):
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return 'D object (name = %s)' % self.name
    __repr__ = __str__
    
print D('wangh') 
# 如果需要将类 作为可迭代的对象，需要实现__iter__(self) 及 next(self) 方法
class E(object):
    def __init__(self):
        self.a = 0
        self.b = 1
                
    def __iter__(self):
        return self
    
    def next(self):
        tmp = self.b
        self.b = self.a + self.b
        self.a = tmp
       # self.a, self.b = self.b, self.a + self.b # 先计算在加上 同上
        if self.a > 100000: 
            raise StopIteration()
        return self.a
    
    def __getitem__(self, n): # 使类可以使用索引取值， 但是需要对传入的参数做类型判断，如切片 isinstance(n, slice) 
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
        # 还有负数等  与之对应的方法__setitem__   __delitem__ 

for n in E():
    print n

print E()[10]
# 对实例进行调用 需要实现 __call__ 方法
class F(object):
    def __init__(self, num):
        self.num = num
        
    def __call__(self):
        return 'Num = %d' % self.num
    
f = F(123)
print f()
# callable 函数  可以判断 对象是否可以被调用
print callable(f)

# 使用 type()函数动态创建类
print '使用 type()函数动态创建类'
# 先定义函数
def fn(self, name = 'world'):
    print 'Hello %s' % name
Hello = type('Hello', (object,), dict(hello = fn)) # 创建Hello class
h = Hello()
h.hello()
# 要创建类 type() 需要传入三个参数
# 1 class 的名称 
# 2 继承的父类集合，如果只有一个 记住  元祖的 ,
# 3 方法名和函数绑定



































    