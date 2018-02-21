# python3网络编程笔记

## 一、TCP/IP简介

​	网络通行本质上是两台计算机上的两个进程间的通信。

​	每个计算机有一个IP地址，IP地址对应的实际是计算机的网络接口，通常是网卡。

​	IP协议负责把数据从一台计算机通过网络发送到另一台计算机，数据被分成小块发送出去；TCP协议建立在IP协议上，TCP协议故则在两台计算机间建立可靠连接，对每个IP包编号确保按顺序收到，丢失会自动重发。TCP协议是许多高级网络协议的基础。即：IP协议负责分解，TCP协议保证重组。

​	一个TCP报文含有源IP地址、原端口和目标端口。

​	每个网络进程为了和另一台计算机建立链接，都会向操作系统申请唯一的端口号，一个进程也可能同时与多个计算机建立链接，因此它会申请很多端口。



## 二、TCP编程

​	套接字（Socket）表示“打开了一个网络链接”，而打开一个Socket需要目标计算机的IP地址和端口号，再指定协议类型。

### 1、客户端

​	创建TCP连接的时候,，主动连接方成为客户端，被动相应方称为服务器。

```python
import socket

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('www.sina.com.cn', 80))
```

​	创建`socket`实例时，第一个参数是地址族，`AF_INFT`指定IPv4协议，如果使用更先进的IPv6，就指定`AF_INFT6`；第二个参数`SOCK_STREAM`指定面向流的TCP协议。

​	创建连接，需要知道目标的IP地址和端口号。使用域名可以自动转换到IP地址；然后作为服务器，端口号是根据服务类型而定的，`80`是web服务的标准端口。此外，端口号小于1024的是Internet服务的标准端口，大于1024的端口可以任意使用。

​	TCP连接创建的是双向通道，但是先后协调方式要根据具体协议而定，如HTTP协议要求客户端发送请求给服务器，服务器收到后发送数据给客户端。

```python
# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

# 关闭连接
s.close()
```

​	接收数据时，调用`recv(max)`方法，指定一次接收的最多字节数，反复接收到没有数据就结束，使用`close`方法关闭Socket，开始保存数据。

```python
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)
```

**搭建客户端步骤如下：**

​	1、创建Socket实例；

​	2、用实例建立连接`connect`，传入目标地址和端口，要注意参数是一个元组;

​	3、用实例接收数据`recv`，进行一系列处理；

​	4、关闭实例`close`，断开连接。

###2、服务器

​	服务器进程首先要绑定一个端口并监听来自其他客户端的连接。如果某个客户端连接过来了，服务器就与该客户端建立Socket连接。

​	服务器会打开固定端口（如80）监听，对每个客户端访问创建Socket连接。每个Socket拥有四项：服务器和客户端各自的地址和端口。

```python
import socket

# 先创建一个Socket，写好协议类型
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

​	对Socket要绑定监听的地址和端口。服务器可能有多块网卡，可以绑定一块的IP地址上，也可以使用特殊的IP地址：`0.0.0.0`表示所有的网络地址；`127.0.0.1`表示本机地址，此时客户端必须在本机内。

```python
# 监听端口，非标准服务不应当使用1024以下的端口
s.bind(('127.0.0.1', 9999))

# 开始监听，传入等待连接的最大数量
s.listen(5)
print('Waiting for connection...')
```

​	服务器通过一个永久循环来接受来自客户端的连接，`accept()`会等待并返回一个客户端的连接。

```python
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
```

​	每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接，使用的`accept`方法返回的是一个`(client, address)`的格式：前者是一个客户套接字，后者是地址。

```python
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)
```

​	连接建立后，服务器首先发一条欢迎消息，然后等待客户端数据，并加上`Hello`再发送给客户端。如果客户端发送了`exit`字符串，就直接关闭连接。

​	要测试这个服务器程序，我们还需要编写一个客户端程序：

```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
```

**搭建服务器步骤如下：**

​	1、创建Socket实例；

​	2、用实例绑定监听地址和端口`bind`，要注意参数也是一个元组；

​	3、用实例开始监听`listen`，传入等待连接的地址最大数量；

​	4、使用循环多线程模式处理新连接`accept`；

​	5、关闭Socket实例`close`。

## 三、UDP编程

​	TCP建立可靠连接，且通信双方都以流的方式发送数据。相对TCP，UDP则是面对无连接的协议。

​	使用UDP只要直到对方的IP地址和端口号，就可以直接发数据包，但是不确保到达。UDP相对于TCP的优点在于快速，适合不是非常重要的数据，如游戏数据，在线视频播放。

​	创建一个UDP协议服务器首先需要绑定端口：

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('127.0.0.1', 9999))
```

​	创建实例时`SOCK_DGRAM`指定了这个Socket的类型是UDP，不需要`listen()`方法，可以直接接收来自任何客户端的数据：

```python
print('Bind UDP on 9999...')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)
```

​	`recvfrom()`方法返回数据和客户端的地址与端口，这样，服务器收到数据后，直接调用`sendto()`就可以把数据用UDP发给客户端（此处略去多线程）。

​	客户端使用UDP时，先仍然创建基于UDP的Socket，然后不需调用`connect()`，直接通过`sendto()`给服务器发数据：

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))
s.close()
```