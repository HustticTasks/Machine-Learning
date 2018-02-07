# python线程进程笔记

## 一、导入

​	对于操作系统来说，一个任务就是一个进程（Process），在一个进程内部要同时运行多个“子任务”，称之为线程（Thread）。多进程和多线程的执行方式都是快速轮流占用CPU。

​	先前编写的python程序都是执行单任务的进程，即只有一个线程的进程。有三种解决方法：多进程模式、多线程模式、多进程+多线程模式。

​	处理同步和数据共享的问题。



## 二、多进程

###1、分支Folk

​	Unix/Linux操作系统提供了一个`fork()`系统调用，调用一次，返回两次；因为系统自动把当前进程（父进程）复制了一份（子进程），在父进程和子进程。

​	子进程永远返回`0`，父进程返回子进程的ID。因为父进程可以folk出很多子进程，所以父进程要记下每个进程的ID，而子进程只需要调用`getppid()`就可以拿到父进程的ID。

```python
import os

print('Process (%s) start...' % os.getpid())
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
```

​	运行结果如下：

```python
Process (876) start...
I (876) just created a child process (877).
I am child process (877) and my parent is 876.
```

​	通过`fork`调用，一个进程在接到新任务时可以复制出一个子进程来处理新任务，从`folk`开始子进程会复制父进程的数据信息，而后程序就会分两个进程继续运行后面的程序，这就是`folk`（分叉）的由来。

​	*PS：由于windows没有`folk`调用，windows上无法运行如下代码。*

###2、跨平台多进程模块multiprocessing

​	`multiprocessing`模块是跨平台版本的多进程模块，可以照顾到没有`folk`调用的windows系统。`multiprocessing`模块提供了一个`Process`类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：

```python
from multiprocessing import Process
import os

# 子进程要执行的代码，写成函数的形式
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

# 执行的代码
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
```

​	创建子进程时，只需要传入一个执行函数和其参数，创建一个`Process`实例，用`start()`方法启动，`join()`方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

```python
Parent process 928.
Process will start.
Run child process test (929)...
Process end.
```

### 3、进程池Pool

​	使用进程池批量创建子进程。

```python
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
```

​	对`Pool`对象调用`join()`方法会等待所有子进程执行完毕，调用`join()`之前必须先调用`close()`，调用`close()`之后就不能继续添加新的`Process`了。

​	请注意输出的结果，task `0`，`1`，`2`，`3`是立刻执行的，而task `4`要等待前面某个task完成后才执行，因为`Pool`会有默认大小，表示最多同时执行的进程，该值是电脑CPU的核数，可以更改。

```python
Parent process 669.
Waiting for all subprocesses done...
Run task 0 (671)...
Run task 1 (672)...
Run task 2 (673)...
Run task 3 (674)...
Task 2 runs 0.14 seconds.
Run task 4 (673)...
Task 1 runs 0.27 seconds.
Task 3 runs 0.86 seconds.
Task 0 runs 1.41 seconds.
Task 4 runs 1.91 seconds.
All subprocesses done.
```

### 4、子进程subprocess

​	很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。`subprocess`模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。

#### 4.1、运行外部命令

​	`subprocess.call(command)`方法可用于执行一个外部命令，该方法不能返回执行的结果，只能返回执行的状态码：成功`0`或错误`非0`。command可以是列表，也可以是字符串，后者需要使用参数`shell=True`。

```python
# 也可为subprocess.call("ls -l", shell=True)
>>> subprocess.call(['ls','-l'])
total 8
drwxrwxr-x 4 ws ws 4096 Nov 25 13:50 MonitorSystem
drwxrwxr-x 2 ws ws 4096 Feb 19 10:09 tmp
0 # 返回的状态码
```

#### 4.2、错误处理

​	`subprocess.check_call()`方法，`call`方法返回一个状态码，通过`check_call()`函数检测命令的执行结果，不成功则返回`subprocess.CalledProcessError`异常。

​	可以使用`try...except...`句式来避免错误。

#### 4.3、捕获输出结果

​	`subprocess.check_output()`方法。使用`call`方法启动的进程输入输出会绑定到父进程的输入和输出，调用程序无法获得命令的输出结果。可以捕获用`call`方法启动的进程的输出结果。

```python
>>> output=subprocess.check_output("ls -l",shell=True)
>>> output
b'total 8\ndrwxrwxr-x 4 ws ws 4096 Nov 25 13:50 MonitorSystem\ndrwxrwxr-x 2 ws ws 4096 Feb 19 10:09 tmp\n'
# 对字节类型使用decode方法将其转化为utf-8格式
>>> print(output.decode('utf-8'))
total 8
drwxrwxr-x 4 ws ws 4096 Nov 25 13:50 MonitorSystem
drwxrwxr-x 2 ws ws 4096 Feb 19 10:09 tmp
```

#### 4.4、直接处理管道



#### 4.5、捕获错误输出



###5、进程间通信

​	`Process`之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的`multiprocessing`模块包装了底层的机制，提供了`Queue`、`Pipes`等多种方式来交换数据。



##三、多线程

### 1、启动线程

​	线程是操作系统直接支配的执行单元。Python的标准库提供了两个模块：低级模块`_thread`和高级模块`threading`，后者对前者进行了封装，只需要使用后者即可。

​	启动一个线程，只需把一个函数传入并创建`Thread`实例，然后调用`start()`开始执行。

```python
import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')# 此处命名
# 与进程实例相同的使用方法
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

```

​	任何进程都会启动一个线程，我们称之为主线程，主线程可以启动新的线程。`threading`模块的`current_thread()`函数永远返回当前线程的实例，主线程实例名为`MainThread`，子线程实例的名字在创建时使用参数`name`指定，然而名字除了打印并没有什么卵用，执行结果为：

```python
thread MainThread is running...
thread LoopThread is running...
thread LoopThread >>> 1
thread LoopThread >>> 2
thread LoopThread >>> 3
thread LoopThread >>> 4
thread LoopThread >>> 5
thread LoopThread ended.
thread MainThread ended.
```

​	**多线程模式的格式为：**

​	1、创建新线程实例，初始化的属性`target=函数名, args=实参元组`，还有`name`参数可以指定子进程名。

​	2、使用`start`方法开始。

​	3、使用`join`方法等待所有线程结束，能够合并所有线程。

### 2、锁

​	多进程中，每个进程相互独立，有独立的作用域；而多线程共享一个作用域。

​	因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。

```python
# 这是一个两个线程同时改变一个变量的程序
import time, threading

# 假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
```

​	CPU执行的是机器语句，如`balance = balance + n`也要拆分为两步：1、计算`balance + n`，存入临时变量中；2、将临时变量的值赋给`balance`。也就可以视作如下：

```python
x = balance + n
balance = x
```

​	由于t1和t2交替运行，可能出现下面的情况

```python
初始值 balance = 0

t1: x1 = balance + 5  # x1 = 0 + 5 = 5

t2: x2 = balance + 8  # x2 = 0 + 8 = 8
t2: balance = x2      # balance = 8

t1: balance = x1      # balance = 5
t1: x1 = balance - 5  # x1 = 5 - 5 = 0
t1: balance = x1      # balance = 0

t2: x2 = balance - 8  # x2 = 0 - 8 = -8
t2: balance = x2   # balance = -8

结果 balance = -8	 #按顺序执行应该为0
```

​	确保`balance`计算正确，就要给`change_it()`上一把锁，同一时间只有一个进程能拥有。通过`threading.Lock()`可以创建一个锁，给函数上好锁后，每个进程执行时，就令其得到锁：

```python
balance = 0
lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
```

​	含锁代码只能以单线程模式执行，阻止了多线程并发执行；存在多个锁时，不同线程持有不同锁，并试图取得对方持有的锁时，可能形成死锁，导致多个线程全部挂起下不来。

### 3、多核CPU

​	在解释器执行代码时，任何线程执行前必须先获得GIL锁，然后每执行100条字节码，就会自动释放GIL锁，让别的线程有机会执行。所以Python本质上还是单线程语言，在多线程模式下依然只能利用一个核。

​	如果想利用多核，应该考虑多进程实现多核任务。多个进程有各自独立的GIL锁，不会干扰。

*PS：所一即使一张桌子上有几个人吃菜，筷子却只有一双。*

## 四、ThreadLocal	

​	`ThreadLocal`解决了参数在一个线程中各个函数之间互相传递的问题。

​	方法1：多线程环境中，一个线程使用自己的局部变量比使用全局变量好。但是这样函数调用很麻烦，要把值一层一层传递下去。

```python
def process_student(name):
    std = Student(name)
    # std是局部变量，但是每个函数都要用它，因此必须传进去：
    do_task_1(std)
    do_task_2(std)

def do_task_1(std):
    do_subtask_1(std)
    do_subtask_2(std)

def do_task_2(std):
    do_subtask_2(std)
    do_subtask_2(std)
```

​	方法2：用一个全局`dict`存放所有的`Student`对象，然后以`thread`自身作为`key`获得线程对应的`Student`对象。这样人为地给每个线程创建了一个副本。

```python
global_dict = {}

def std_thread(name):
    std = Student(name)
    # 把std放到全局变量global_dict中：
    global_dict[threading.current_thread()] = std
    do_task_1()
    do_task_2()

def do_task_1():
    # 不传入std，而是根据当前线程查找：
    std = global_dict[threading.current_thread()]
    ...

def do_task_2():
    # 任何函数都可以查找出当前线程的std变量：
    std = global_dict[threading.current_thread()]
    ...
```

​	方法3：使用`ThreadLocal`

```python
import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
```

​	执行结果为：

```python
Hello, Alice (in Thread-A)
Hello, Bob (in Thread-B)
```





## 五、进程与线程







## 六、分布式进程

