# 定义：
class Dog():
    """类文档注释"""

    __age = 0       # 定义类私有属性，以两个下划线开头
    name = 'lisi'   # 定义类公共属性

    def __init__(self, name, age):  # 构造函数，只能有一个
        self.name = name;
        self.age = age;

    # 定义类公共方法
    def func(self):  # 每一个类方法第一个参数都是self  代表类实例本身，方法调用时自动传递
        print(self.name)

    # 定义类私有方法，以两个下划线开头
    def __func2(self):
        print(self.age)



# 实例化：
dog = Dog("w", 12);
dog.name = "h";  # 怎么防止直接修改属性？

# 继承：
class Car():
    def __init__(self, name):
        self.name = name;


class ECar(Car):
    def __init__(self, name):
        super.__init__(name);  # 初始化父类


#覆盖方法：
# 子类定义父类同名函数

# 动态属性需要继承object类
class MyClass(object):
    def __init__(self):
        self.__param = None
        self.__param2 = None

    def getParam(self):
        print('getParam: %s' % self.__param)
        return self.__param

    def setParam(self, value):
        print('setParam: %s' % self.__param)
        self.__param = value

    def delParam(self):
        print('delParam: %s' % self.__param)
        del self.__param

    param = property(getParam, setParam, delParam)

    # 方法2：使用@property修饰

    @property # getter
    def param2(self):
        print('get param2: %s' % self.__param2)
        return self.__param2

    @param2.setter
    def param2(self, value):
        print('set param2: %s' % self.__param2)
        self.__param2 = value

    @param2.deleter
    def param2(self):
        print('del param2: %s' % self.__param2)
        del self.__param2

if __name__ == '__main__':
    cls = MyClass()
    cls.param = 10  # setParam
    print('current cls.param: %s' % cls.param) # getParam
    del cls.param # delParam

    cls.param2 = 101  # setter
    print('current cls.param2: %s' % cls.param2) # getter
    del cls.param2 # deleter