#!/usr/bin/env python
# -*- coding: utf-8 -*-

# namedtuple()函数创建自定义的tuple
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(101, 2)
print p.x
print p.y

# deque双端队列
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print q

# defaultdict 无key时返回默认值
from collections import defaultdict
d = defaultdict(lambda : 'N/A')
d['key1'] = 'abc'
print d['key1']
print d['key2']

# OrderedDict 顺序key字典
from collections import OrderedDict
od = OrderedDict()
od['oz'] = 2
od['oc'] = 3
od['oa'] = 1
print od.keys()

# Counter 简单计数器
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] += 1
print c
























