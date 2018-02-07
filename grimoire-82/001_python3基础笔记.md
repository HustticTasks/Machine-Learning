# Python3基础笔记

## 一、变量与数据类型

1、输入数据 `int(input("提示内容"))`

2、输出格式 `print("f = {:5d}, c = {:7.2f}".format(fahreheit , celsius))`

​	{:5d}表示替换为5个字符宽度的整数，宽度不足则使用空格填充。

3、单行多个变量

​	下列代码能够交换两个数字的值。

```python
a , b = 45,54
a , b = b , a
```

​	元组封装与元组拆封。

```python
>>> data = ("human", "binder", "John")
>>> race, Class, player = data
>>> name
'human'
>>> Class
'binder'
>>> player
'John'
```



 ## 二、运算符和表达式

1、逻辑运算：与C语言相区别，使用 and、or、和not。

2、类型转换：要记得int()、float()、和str() 在整形、浮点型和字符型数据间转换的用法，还可以用list()将字符串转化为列表。



## 三、控制流if-else 和 循环

python中很多值都是具有布尔意义的，可以利用这一点写的优雅一点。

print()内置的end参数默认值为'\n'，即在每次输出的末尾加上一个换行符。

输出中常用到的分割方法 `x = "-" * 10`



## 四、数据结构

###1、列表

```python
[]
```

​	记得几个常方法：append(b)、insert(a,b)、count(b)、remove(b)、extend(L)、reverse()，其中L表示列表，a表示下标，b表示下标对应的值。

​	删除元素：pop(i)弹出下标对应的元素，remove(value)值对应的元素。

​	形成栈：使用pop()方法逐步弹出尾部元素。

###2、列表生成式

```python
[[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]]
```

​	由三部分组成：表示元素结构的”框架结构“，用for表示迭代范围的“迭代结构”，表示if表示条件判断的“条件结构”。

###3、元组

```python
（）
```

###4、集合

```python
{}
```

​	用add()方法和pop()方法，分别添加元素和弹出元素。（由于集合内部是不重复且无序的，所以弹出对元素相对排序后的最后一个元素）

###5、字典

```python
{:}
```

删除元素 `del dict[key]` 。

判断元素 `key in dict` （具有布尔类型）。

遍历字典 `dict.items()` 返回一个元组（key, value）类型的列表。

判断元素并取值 `dict.get(key, default)`

判断元素并取值和修改 `dict.setdefault(key, default)`



## 五、字符串

###1、字符串前缀

​	r：表示raw string，不识别转义。

​	b：表示生成字节序列对象，在需要按字节序列发送数据时使用。

###2、字符串修改

​	修改大小写：单词首字母大写 title()，全部大写upper()，全部小写lower()，交换大小写swapcase()。

​	分割字符串 `string.split('以什么分割')` ，返回一个列表。

​	拼接字符串 `"用什么拼接".join(List)` ，返回一个列表。

文本搜索：find()返回下标，startswith()和endswith()检查开头结尾，具有布尔类型。



## 六、函数

​	有4类参数：普通参数、默认参数、可变参数、关键字参数。

###1、变量作用域

​	只有模块、类和函数会引入新的作用域，代码块不会。

​	有四种作用域，按查询的先后次序为：局部作用域（Local）、闭包函数外作用域（Enclosing）、全局作用域（Global）和内建作用域（Built-in）。

​	在函数中 `global` 和 `nonlocal`	使局部变量分别能修改全局变量和外层非全局变量，类似C语言中的extern引用声明。

###2、默认参数

​	默认值只能被赋值一次，如下声明：

```python
def f(a, data=[]):
	data.append(a)
    return data
```

​	其调用的结果为：

```python
>>> print(f(1))
[1]
>>> print(f(2))
[1, 2]
>>> print(f(3))
[1, 2, 3]
```

​	可见每次调用之后都会“积累”，这是因为data“指向”的数据是可变的，达到了类似于C语言中static的效果。

​	如上默认参数必须指向不变对象！可以通过将data指向关键字None，然后在函数体内部完成赋值来实现。

###3、可变参数

​	定义：用 `*List` 的格式来定义可变参数，表示将可变数量的参数组装成为一个元组。

​	调用：对于多个参数可以直接传入，如果是将一个列表/元组内的所有元素传入，则使   `*列表/元组` 的格式。

###4、关键字参数

​	定义：用 `**kw` 的格式来定义关键字参数，表示将 `key = value` 格式的参数组装成一个字典。

​	调用：与默认参数相区分时，为了表示，即使每有可变参数，也要在声明函数时补上 `*` 空可变参数。

###5、高阶函数

​	以函数作为参数，返回函数的函数。(因为python内支持嵌套定义)

如：

​	`map(函数f，迭代器)` 将函数f应用在迭代器中的每一个对象上，并返回新的迭代器。



## 七、模块

​	使用 `import 模块名` 语句后会有同名指针指向相应模块。

###1、身份判断

```python
if __name__=='__main__':
    f()
```

​	模块有两种使用方法：直接运行模块、被交互式环境或其他程序调用；只有是自己调用自己时，才是 `__main__` 。

###2、作用域

​	我们希望封装模块，一些函数和变量应该被屏蔽，有如下格式：

`__xxx__` ：特殊变量，能被直接引用。

​    `_xx` ：私有变量和函数，不应该被直接引用。



## 八、面对对象编程

###1、类和实例

​	使用 `__init__` 方法声明类的属性，即在方法内部把各种属性绑定到 `self` ，`self`指向创建的实例本身。

​	创建实例时，必须传入与 `__init__` 方法相匹配的参数。 

```python
class Student(object):
  
	def __init__(self, name, score):
		self.name = name
		self.score = score
```

​	数据封装：类内部定义的函数，除了第一个参数是 `self` 之外与普通函数一样。

###2、访问限制

​	双下划线开头的属性为私有属性，python解释器会改变它们的名字使其无法在外部被访问。

​	单下划线开头可以访问，但是不建议直接访问。

​	双下划线开头结尾的是可以直接访问的特殊变量，不应该以这种格式命名自己的变量。

```python
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
```

​	以防万一：增加 `get_name` 和 `get_score` 方法，通过内部手段获得 `__name` 和 `__score` ；修改亦如此。

```python
def get_name(self):
	return self.__name
def get_score(self):
	return self.__score
 
```

###3、继承和多态

​	定义一个class时，可以从某个现有的class继承；它们之间是子类和父类的关系。

```python
class Dog(Animal):
    pass
```

​	子类获得父类的全部功能，存在相同方法时，子类会覆盖父类的相应方法。

​	多态：一个实例属于它被定义的类，也属于该类的父类和超类。如下函数：

```python
#存在animal类，拥有方法run()；还存在其子类cat和dog，覆盖了方法run()
#接受一个animal类型的变量
def run_twice(animal):
    animal.run()
    animal.run()
```

​	如果传入的是cat和dog的实例，就会使用覆盖后的相应方法。故多态的优点在于新增一个 `Animal` 的子类，不需要对 `run_twice()` 作任何修改；即：对扩展开放，对修改封闭。

###3+、静态语言&动态语言

​	对于静态语言，如果需要传入 `Animal` 类型，则传入的对象必须是 `Animal` 类型或者它的子类，否则，将无法调用 `run()` 方法。

​	对于Python这样的动态语言，只需要保证传入的对象有一个 `run()` 方法就可以。

​	这就是动态语言的“鸭子类型”，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

###4、获得对象信息

​	类型判断 ：`type(obj)` 传入一个实例，可以返回它对应的Class类型。可以用于构建布尔表达式。

​	归属判断：`isinstance(a, A)`  判断实例a是否在类A中，A可以是一个元组，表示是否在A中任何一个类中；具有布尔特性。 

​	列出信息：`dir(obj)` 返回一个字符串list，含有一个对象的所有属性和方法。

​	对象操作：三种对象操作，分别表示判断，设置，获取。

```python
hasattr(obj, 'x') #有属性'x'吗？
setattr(obj, 'y', 19) #设置一个属性'y'
getattr(obj, 'y') #获取属性'y'
#可以传入一个default参数，如果属性不存在，就返回默认值
getattr(obj, 'z', 404) #获取属性'z'，如果不存在，返回默认值404
```

###5、实例属性和类属性

​	实例属性：创建实例时，通过实例变量绑定；或声明类的时，在 `__init__` 方法中通过 `self` 变量绑定。

​	类属性：在class中直接定义。

​	每个实例都有自己的实例属性，所有实例共用类属性（类属性是属于类自己的）。

```python
class Student(object):
    count = 0 #类属性
    
    def __init__(self, name):
        self.name = name #实例属性
```

​	注意实例属性不要与类属性重名，否则会屏蔽类属性。建议用 `Student.count` 访问类属性count。





## 九、面对对象高级编程

### 1、限制实例属性

​	可以给实例动态绑定属性和方法，但是为了给所有的实例都绑定上新方法，可以给class动态绑定方法：

```python
>>> def set_score(self, score): #写出一个新方法
...     self.score = score
...
>>> Student.set_score = set_score #把这个方法绑给一个class
```

​	如果要限制创建实例的属性，可以使用class的特殊变量 `__slots__` 。

```python
class Student(object):
    __slots__ = ('name', 'age') #用tuple定义允许绑定的属性名称
```

​	注意 `__slots__` 只对当前类起作用，对子类不起作用。

###2、@property

​	在绑定属性时，如果直接把属性暴露出去，为了检查参数（如限制范围）就需要补充方法。为了既能检查参数，又能像属性一样简单，可以使用装饰器。

​	装饰器（decorator）中的内置 `@property` 可以把方法像属性一样调用。

```python
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
```

​	一个属性拥有“ 读”和“写”两个功能，我们用自己的getter和setter两个方法实现。

​	通过添加 `@property` 把一个getter方法变成属性，同时创建一个新的装饰器 `@score.setter` ，把它添加在一个setter方法前面；至此通过两个方法实现了一个属性操作。

```python
>>> s = Student()
>>> s.score = 60 # 实际转化为s.set_score(60)
>>> s.score # 实际转化为s.get_score()
60
>>> s.score = 9999
Traceback (most recent call last):
  ...
ValueError: score must between 0 ~ 100!
```

​	还可以定义只读属性，即没有“写”功能，只定义getter方法，不定义setter方法。

​	*PS：在两个方法中给实例绑定了一个属性，这个属性作为私有属性应该以 `_` 开头，同时要注意类中 `__slots__` 对新增属性的影响。*

### 3、多重继承

​	从多个类中继承，服从两条原则：子类在父类前；依序检查。

### 4、定制类

**4.1、显示实例信息**

```python
>>> print(Student('Michael'))
<__main__.Student object at 0x109afb190>
```

​	在交互式环境使用print或直接查看实例信息时会出现上面的丑陋描述。我们在类中有两个特殊方法用于显示这种信息：`__str__()` 和 `__repr__()` ，前者在print(实例)中显示，给用户显示；后者在直接查看实例时显示，给开发人员调试用。

​	`__str__()` 和 `__repr__()` 其实都一样，所以可以使用下面定义。

```python
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__ #偷懒写法
```

**4.2、依次迭代的实例**

​	创建一个可用于（包括但不限于for循环的）循环的迭代对象，使用 `__iter__()` 方法返回下一个迭代对象，然后不断调用该迭代对象的 `__next__()` 方法拿到循环的下一个值，直到出现 `StopIteration` 错误。

​	以下面的斐波那契数列迭代对象为例。

```python
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值	
```

**4.3、下标访问的实例**

​	上面的Fib实例能作用于for循环，但是只能依次返回下一个值，不能像list一样用下标访问。为了实现该功能，需要 `__getitem__()` 方法。

```python
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
```

​	如上能像list一样用下标访问数列的另一项。

​	但是如果要实现list的切片方法，还需要对 `__getitem__()` 方法的内容进行补充。如下：

```python
class Fib(object):
    def __getitem__(self, n):
    ......
		if isinstance(n, slice): #n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
```

**4.4、无中生有的属性和方法**

​	当调用不存在的类属性和方法时会发生报错，可以使用 `__getattr__()` 动态返回属性和方法。

```python
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
    	if attr=='age': 
          	return lanmda:25 #动态返回函数
        if attr=='score':
            return 99 #动态返回属性
		raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr) #只响应上面可能出现的，对没有预料的直接报错
```

​	已有的属性不会到attr中查找，一旦有 `__getattr__()` 存在，会对任意属性和方法都返回 `None` ，这是该方法的默认值，如果要求只相应特定的几个属性，就应当抛出错误。

**4.5、调用实例**

​	直接按照函数的格式调用实例，只需定义一个 `__call__()` 方法，通过该方法，我们让对象和函数间的关系变得模糊了。

```python
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
```

​	调用时如下：

```python
>>> s()
My name is Michael.
```

​	使用 `callable()`函数 ，我们可一判断一个对象是否能调用。

### 5、枚举类

###6、元类





## 十、错误、调试和测试

### 1、错误处理

**1.1、处理机制**

​	内置 `try...except...finally...` 错误处理机制。

​	完整格式即 `try...except...except...else...finally...`

```python
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')
```

​	`try` 语句块中如果错误，会直接跳转到 `except` 语句块，不论有无错误如果有 `finally` 则继续执行。

​	可以添加多个 `except` 语句块来分别处理不同错误，还可以在 `except` 语句块群后添加 `else` 语句块，当没有错误发生时，会执行 `else` 语句块。如：

​	不同的错误也有继承关系，指定捕捉一种错误会把它的子类错误也一网打尽。在写 `except` 语句块群时要注意子类在前，父类在后，否则错误会被前面的父类一网打尽。

**1.2、调用栈**

​	如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。如：

```python
# err.py:
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    bar('0')
main()
```

​	报错为：

```python
$ python3 err.py
Traceback (most recent call last):#表明这是错误的跟踪信息
  File "err.py", line 11, in <module>#调用main()出错了，在11行，原因如下...
    main()
  File "err.py", line 9, in main
    bar('0')
  File "err.py", line 6, in bar
    return foo(s) * 2
  File "err.py", line 3, in foo#找到错误源头
    return 10 / int(s)
ZeroDivisionError: division by zero#打印最终错误
```

**1.3、记录错误**

​	Python内置的 `logging` 模块可以非常容易地记录错误信息：

```python
# err_logging.py
import logging

def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)#用此行代码将错误记在logging中

main()
print('END')
```

​	程序打印完错误信息后会继续执行，并正常退出：

```python
$ python3 err_logging.py
ERROR:root:division by zero
Traceback (most recent call last):
  File "err_logging.py", line 13, in main
    bar('0')
  File "err_logging.py", line 9, in bar
    return foo(s) * 2
  File "err_logging.py", line 6, in foo
    return 10 / int(s)
ZeroDivisionError: division by zero
END
```

**1.4、抛出错误**

​	错误是class，捕获一个错误就是捕获到该class的一个实例。

​	我们可以自定义错误类型



###2、调试

​	介绍调试的三种方法：

**2.1、打印**

​	用`print()`把可能有问题的变量打印出来，但是将来还得删掉它，十分不便。

**2.2、断言**

​	assert后接布尔表达式，如果是False则断言失败，`assert` 语句本身就会抛出`AssertionError` 。

```python
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!' #如果n=0,则抛出错误，并打印'n is zero!'
    return 10 / n

def main():
    foo('0')
```



​	启动Python解释器时使用 `-0` 参数可以关闭所有断言，将 `assert` 等效为 `pass` 语句。

**2.3、记录**

​	使用 `logging` 模块，不会抛出错误，还可输出到文件。

```python
import logging
logging.basicConfig(level=logging.INFO) #指定输出级别

s = '0'
n = int(s)
logging.info('n = %d' % n) #起到输出文本的作用
print(10 / n)
```

​	以下为输出结果：

```python
$ python err.py
INFO:root:n = 0 #这是info输出的信息
Traceback (most recent call last): #此处开始是报错
  File "err.py", line 8, in <module>
    print(10 / n)
ZeroDivisionError: division by zero
```

**2.4、单步**

​	启动Python调试器pdb，单步运行程序，使用 `python -m pdb 程序名` 。

​	启动后pdb定位到下一步要执行的代码；用到的命令有：`l` 查看代码和进度，`n` 单步执行代码，`p 变量名` 查看变量， `q` 结束调试并退出。

**2.5、断点**

​	导入pdb模块，在可能出错的地方设置一个 `pdb.set_trace()`，就可以设置一个断点，运行代码时会在此暂停并进入pdb调试环境。使用 `c` 继续运行。

##十一、IO编程

### 0、导言

​	程序运行时数据在内存中驻留，由CPU这个计算核心来执行，涉及数据交换时就需要IO接口。由于CPU和内存的速度远高于外设速度，所以存在速度不匹配，根据CPU是否等待磁盘，分为同步IO和异步IO。

###1、文件读写

​	先open，然后read或write，最后close。文件读写时都可能出现 `IOError` ，出现则 `f.close()` 就不会调用，不论如何都应该正确地关闭文件，使用 `try ... finally` 来实现。

```python
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()
```

​	也能使用更简单的语句，不需要调用 `close()` 方法：

```python
with open('/path/to/file', 'r') as f:
    print(f.read())
```

​	`read()` 读取全部内容（当心内存爆掉）；`read(size)` 读取size个字节的内容； `readline()` 每次读取一行内容（就像水流，依序读取）；`readlines()` 读取每一行并按行返回list。

​	