
# 列表定义
l1 = ['wangh', 'kongl', 'wanghjy']
l2 = ['zhangs', l1]

# 索引
print(l1[0]) # wangh
print(l1[1]) # kongl
print(l1[-1]) # wanghjy
print(l1[-2]) # kongl
print(l2[1][1]) # kongl

# 子集
print(l1[1:2]) # ['kongl']
print(l1[1:]) # ['kongl', 'wanghjy']
print(l1[1:-1]) # ['kongl']
print(l1[:-1]) # ['wangh', 'kongl']

# 常用操作列表函数
print(len(l1)) # 3
print(max(l1)) # wanghjy
print(min(l1)) # kongl

# 列表常用方法
l1.append('zhangs')  # 末尾添加元素
print(l1)
print(l1.count('wangh')) # 1 某个元素在列表中的个数
l1.extend(['123', '234']) # 列表末尾添加另一个列表的元素
print(l1)
print(l1.index('123')) # 4 找出元素第一次出现的索引
l1.insert(4, '555') # 在指定位置插入元素
print(l1)
obj = l1.pop(-2) # 移除并返回列表中的元素,默认为最后一个元素
print(obj) # 123
print(l1)
l1.remove('555') # 移除第一次出现的指定元素
print(l1)
l1.reverse() # 翻转列表
print(l1)
l1.sort() # 对列表进行排序
print(l1)