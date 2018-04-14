import os

class Parent:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def printName(self):
        print("父类的方法")

class Son(Parent):
    #前后都带有双下划线的函数为内置特殊功能函数,比如这个__init__()可以类似理解成java中的Object中的函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printName(self):
        print("子类的方法")

    #前面带一个单下划线的函数为protect函数
    def _printAge(self):
        print("子类的protect方法")
        #只能内部调用私有方法
        self.__printPrivate();

    #前面带双下划线的函数为私有函数
    def __printPrivate(self):
        print("子类的私有方法")

# p = Parent("parent", 50)
# p.printName()

s = Son("son", 20)
s.printName()
s._printAge()

#不能外部调用私有函数
s.__printPrivate()
s.__init__()

