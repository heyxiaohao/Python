
# 定义
dic = {}
dic['name'] = 'wangh'
dic['age'] = 33
dic['famle'] = '男'
print(dic)
dic1 = {
    'name': 'kongl',
    'age': 30,
    'famle': '女',
    'otherdic': {
        'host': '123',
        'ip': '192.168.1.1'
    }
}
print(dic1)

# 根据key获取对象
print(dic['name']) # wangh
print(dic1['otherdic']['ip']) # 192.168.1.1

# 常用操作字典的函数
print(len(dic1)) # 字典元素个数，即key总数
print(str(dic1)) # 输出字典可打印的字符串标识
print(type(dic)) # <class 'dict'>

# 字典常用方法
dic2 = dic
print('dic2,', dic2)
dic.clear() # 删除所有元素，所有引用都变为空
print(len(dic))
print(dic2)

dic3 = dic1.copy() #  返回字典的浅复制
dic3['abc'] = 'aaa'
print(dic3)
print(dic1)

l1 = ['a', 'b', 'c']
dic4 = {}
dic4 = dic4.fromkeys(l1) # 创建一个新字典，以序列的元素做字典的键，val为字典元素的初始值
print(dic4)

print(dic3.get('abc'))  # 返回指定键的值，如果键未找到，则返回default指定的值
print(dic3.get('ab', 'dddd'))

print(dic3.setdefault('ab', '123')) # 与get类似，但如果键不存在，则会添加到字典中，并设置为默认值
print(dic3)

print(dic3.items()) # 以列表形式返回可遍历的(键, 值)元祖列表

print(dic3.keys()) # 以列表形式返回字典的所有键
print(dic3.values()) # 以列表形式返回字典的所有值

dic3.update(dic4) # 把dic2的键值对更新到字典中
print(dic3)