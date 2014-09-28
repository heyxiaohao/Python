#!/usr/bin/env python
# -*- coding: utf-8 -*-

type = 'MySQL'

if type == 'sqlite3':
    # 导入驱动
    import sqlite3
    # 连接到数据库 test.db 如果文件不存在，则会自动创建
    conn = sqlite3.connect('test.db')
    # 创建一个cursor
    cursor = conn.cursor()
    # 执行创建表
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    # 执行插入数据
    cursor.execute("insert into user (id, name) values ('1', 'wangh')")
    # 通过rowcount获取影响的行数
    print cursor.rowcount
    # 关闭cursor
    cursor.close()
    # 提交事物
    conn.commit()
    # 关闭connection
    conn.close()
    
    conn1 = sqlite3.connect('test.db')
    cursor1 = conn1.cursor()
    # 执行查询语句
    cursor1.execute("select * from user where id=?", '1')
    # 获取结果集
    value = cursor1.fetchall()
    print value
    cursor1.close()
    conn1.close()

elif type == 'MySQL':
    import mysql.connector
    
    conn = mysql.connector.connect(user = 'root', password = 'wangh', database = 'test', use_unicode = True)
    cursor = conn.cursor()
    #cursor.execute("create table user (id varchar(20) primary key, name varchar(20))")
    # 插入记录  MySQL的占位符为 %s
    cursor.execute('insert into user(id, name) values(%s, %s)', ['1', 'kongl'])
    print cursor.rowcount
    conn.commit()
    cursor.close()
    
    # 查询
    cursor = conn.cursor()
    cursor.execute('select * from user')# where id = %s' % '1')
    values = cursor.fetchall()
    print values
    cursor.close()
    conn.close()
    
    
else:
    pass
    
    
    
    
    
    
    
    
    
    
    
    