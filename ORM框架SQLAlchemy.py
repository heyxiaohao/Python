#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 用于将数据库表结构用 对象表示出来

# 导入
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey

# 创建对象的基类
Base = declarative_base()

# 定义User对象
class User(Base):
    # 表的名字
    __tablename__ = 'user'
    
    # 表的结构
    id = Column(String(20), primary_key = True)
    name = Column(String(20))
    
# 初始化数据库连接
# 字符串表示连接信息：数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名
engine = create_engine('mysql+mysqlconnector://root:wangh@localhost:3306/test')
# 创建DBSession类型
DBSession = sessionmaker(bind = engine)
# 初始化完成

# 添加记录
# 创建session对象
session = DBSession()
# 创建User对象
new_user = User(id = '5', name = 'Bob')
# 添加到session
session.add(new_user)
# 提交及保存到数据库
session.commit()
# 关闭
session.close()

# 查询记录
# 创建session
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one 是返回为一行，all则返回所有行
user = session.query(User).filter(User.id == '5').one()
# 打印
print 'type: ', type(user)
print 'name: %s' % user.name
session.close()

# 如果一个User拥有多个Book，则可以对那个一一对多关系
class User(Base):
    __tablename__ = 'user'
    
    id = Column(String(20), primary_key = True)
    name = Colum(String(2))
    
    # 一对多
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'
    
    id = Column(String(20), primary_key = True)
    name = Column(String(20))
    # ‘多’的一方book表是通过外键关联到user表
    user_id = Column(String(20)), ForeignKey('user.id')
# 当我们查询一个User对象时，该对象的books属性将返回一个包含若干个Book对象的list，这会不会影响效率，因为我值查询User，可能并不关心Book















