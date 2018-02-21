# python3基础知识增补

## 一、collections模块

### 1、Counter

​	`Counter` 是一个有助于 *hashable* 对象计数的 dict 子类。其实例可以实现动态添加，在访问不存在的键时有默认值`0`。

​	`most_common()` 方法返回最常见的元素及其计数，`elements()` 的、方法返回的序列中，依照计数重复元素相同次数。可以使用常见的函数如`sorted`生成键的排序列表，`sum`求和等。

````python
# elements方法示例
>>> c = Counter(a=4, b=2, c=0, d=-2)
>>> list(c.elements())
['b','b','a', 'a', 'a', 'a']
# most_common方法示例
>>> Counter('abracadabra').most_common(3)
[('a', 5), ('r', 2), ('b', 2)]
````

### 2、defaultdict

​	即使`defaultdict`对象不存在的键，会自动创建一个空列表作为其值。

### 3、namedtuple

​	命名元组对元组每个位置赋予意义。

```python
>>> Point = namedtuple('Point', ['x', 'y'])  # 定义命名元组
>>> p = Point(10, y=20)  # 创建一个对象
>>> p
Point(x=10, y=20)
>>> p.x + p.y
30
>>> p[0] + p[1]  # 像普通元组那样访问元素
30
>>> x, y = p     # 元组拆封
```



## 二、PEP8代码风格指南

​	https://www.shiyanlou.com/login?next=%2Fcourses%2F596%2Flabs%2F2049%2Fdocument



## 三、迭代器、生成器、装饰器

### 1、迭代器（Iterator）

​	迭代器对象需要支持两种方法，迭代器是一种“鸭子类型”。

​	`__iter__()`，返回迭代器对象自身。用在 `for` 和 `in` 语句中。

​	`__next__()`，返回迭代器的下一个值。如果没有下一个值可以返回，那么应该抛出 `StopIteration` 异常。	

```python
lass Counter(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        #返回下一个值直到当前值大于 high
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1
```

​	迭代器只能使用一次，在循环中最终会抛出相同异常，应该使用`try...finally...`语句来控制。

### 2、生成器（Generator）

​	含有`yield`关键字的函数，算作是函数版本的迭代器。

​	每当执行到`yield`语句时返回比那量并将生成器挂起，下一次调用生成器时恢复运行并执行到下一个`yield`语句。

​	*PS:使用生成器来进行惰性求值。可以避免在内存中加载所有数据，通过生成器一次传递一部分。*

​	创建可重复使用生成器的方式是不保存任何住那港台的基于对象的生成器，任何含有`__iter__`方法的类都可以用作对象生成器。

```python
# 这是一个有生成范围的类
>>> class Counter(object):
...     def __init__(self, low, high):
...         self.low = low
...         self.high = high
...     def __iter__(self):
...          counter = self.low
...          while self.high >= counter:
...              yield counter
...              counter += 1
```

​	还可以使用生成器表达式，与列表表达式的格式相同，但是使用圆括号。生成器表达式也只能使用一次。

```python
>>> g = (x*x for x in range(0,10))
>>> sum(g)
285
>>> sum(g)
0
```

###3、闭包

​	闭包是由另外一个函数返回的函数，使用闭包能去除重复代码。

```shell
# 把一个给定的数字与预定义的一个数字相加
>>> def add_number(num):
...     def adder(number):
...         #adder 是一个闭包
...         return num + number
...     return adder
...
>>> a_10 = add_number(10)
>>> a_10(21)
31
>>> a_10(34)
44
>>> a_5 = add_number(5)
>>> a_5(3)
8
```

### 4、装饰器（Decorator）

​	装饰器用来给一些对象动态地添加一些新的行为。

```python
>>> def my_decorator(func):
...     def wrapper(*args, **kwargs):
...         print("Before call")
...         result = func(*args, **kwargs)
...         print("After call")
...         return result # 返回基底函数
...     return wrapper # 返回加工后的函数
...
>>> @my_decorator
... def add(a, b):
...     #我们的求和函数
...     return a + b
...
>>> add(1, 3)
Before call
After call
4
```



##四、Virtualenv

​	虚拟python环境是一个能帮助你在本地目录安装不同版本模块的python环境，不许安装所有东西就能开发和测试代码。

```shell
# 在目录中创建名为virt1的环境
$ cd virtual
$ virtualenv virt1
# 激活这个环境
$ source virt1/bin/activate
(virt1)shiyanlou：~/$
# 关闭这个环境
(virt1)$ deactivate
$
```

​	在独立的环境中，安装的第三方库和系统无关，可以在开发项目时保证不影响系统干净。

​	原理为把系统Python复制一份到virtualenv的环境，用命令`source venv/bin/activate`进入一个virtualenv环境时，virtualenv会修改相关环境变量，让命令`python`和`pip`均指向当前的virtualenv环境。



## 五、测试

### 1、单元测试



## 六、项目结构

 ### 1、准备

​	创建一个目录作为整个项目。

###2、主代码

​	创建一个模块（包），将主代码写在`.py`文件中，并加入模块的`__init__.py`文件。

### 3、MANIFEST.in

​	我们要写一个`MANIFEST.in`文件，使用它在`sdist`命令时找出将加入项目源代码压缩包的所有文件。

```in
include *.py
include README.rst
```

​	可以使用`exclude`语句来排除某些文件。

### 4、安装setuptools包

​	使用`virtualenv`模拟环境来安装需要的模块。

### 5、setup.py

​	需要`setup.py`文件来创建源代码压缩包或安装软件。

```python
#!/usr/bin/env python3
"""Factorial project"""
from setuptools import find_packages, setup

setup(name = 'factorial',
    version = '0.1', # 版本号
    description = "Factorial module.", # 描述
    long_description = "A test module for our book.", # 长描述
    platforms = ["Linux"], # 使用平台
    author="ShiYanLou",
    author_email="support@shiyanlou.com",
    url="https://www.shiyanlou.com/courses/596",
    license = "MIT",
    packages=find_packages()
    )
```

### 6、setup.py打包

​	创建一个源文件发布版本，之后会出现两个目录，能在其中的`dist`目录下看到一个tar压缩包。

```shell
$ python3 setup.py sdist
...
$ ls dist/
factorial-0.1.tar.gz
```

​	执行下面命令从源代码安装。

###7、setup.py解包

```shell
$ sudo python3 setup.py install
```

​	*PS:尝试安装代码时使用virtualenv*



## 七、Flask简介

###1、Flask是什么？

​	Flask 是一个 web 框架，属于微框架（*micro-framework*）这一类别，微架构通常是很小的不依赖于外部库的框架。

- [Werkzeug](http://werkzeug.pocoo.org/) 一个 WSGI 工具包
- [jinja2](http://jinja.pocoo.org/) 模板引擎

> **Web服务器网关接口**（**Python Web Server Gateway Interface**，缩写为WSGI）是为[Python](https://zh.wikipedia.org/wiki/Python)语言定义的[Web服务器](https://zh.wikipedia.org/wiki/%E7%B6%B2%E9%A0%81%E4%BC%BA%E6%9C%8D%E5%99%A8)和[Web应用程序](https://zh.wikipedia.org/wiki/%E7%BD%91%E7%BB%9C%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F)或[框架](https://zh.wikipedia.org/wiki/Web%E5%BA%94%E7%94%A8%E6%A1%86%E6%9E%B6)之间的一种简单而通用的[接口](https://zh.wikipedia.org/wiki/%E4%BB%8B%E9%9D%A2_(%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88))。自从WSGI被开发出来以后，许多其它语言中也出现了类似接口。

###2、模板引擎是什么？

​	搭建网站保证风格一致，使用模板可以保证修改应用在所有页面。