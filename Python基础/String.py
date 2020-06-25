
# 字符串定义
s1 = 'abcd'
s2 = "abcd"
s3 = 'a"b"cd'  # 嵌套定义

# 字符索引
c1 = s1[0]  # a
c2 = s1[1]  # b
c3 = s1[-1] # d
c4 = s1[-2] # c

# 截取子串
ss1 = s1[1:3] # bc
ss2 = s1[1:]  # bcd
ss3 = s1[1:-1] # bc
ss4 = s1[:-1] # abc

# 常用方法
s1 = " abc "
print(s1.strip()) # 去除左右空白字符
print(s1.lstrip()) # 去除左边空白字符
print(s1.rstrip()) # 去除右边空白字符
s2 = ',,,abc,,,'
print(s2.strip(',')) # 去除左右指定字符
print(s2.lstrip(',')) # 去除左边指定字符
print(s2.rstrip(',')) # 去除右边指定字符
l1 = ['first', 'second', 'three']
print(s1.join(l1)) # 在参数列表项之间插入本字符串，若只有1项，则不插入
print(s1.find('b')) # 查找字符，返回第一次找到时的索引

# 字符串比较
print('a' < 'b') # True
print('ab' > 'b') # False
print('ab' > 'aa') # True
print('aa' == 'aa') # True

# 获取字符串长度
print(len('abc')) # 3

# 字符串转换
s1 = 'aBcDeF hIjKlM'
print(s1.upper()) # 转换为大写
print(s1.lower()) # 转换为小写
print(s1.swapcase()) # 大小写互转
print(s1.capitalize()) # 首字母大写，其余字符转为小写

# 字符串分割
s1 = 'abc,def,ghi'
print(s1.split(',')) # 按指定字符分割，返回列表
