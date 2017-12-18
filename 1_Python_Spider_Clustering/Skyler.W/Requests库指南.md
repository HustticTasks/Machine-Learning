Requests库指南
#python##爬虫#
可以这样发送一个 HTTP 请求，炒鸡方便。括号里面是作为字符串输入的网址。
>>> r = requests.post("http://httpbin.org/post")
>>> r = requests.put("http://httpbin.org/put")
>>> r = requests.delete("http://httpbin.org/delete")
>>> r = requests.head("http://httpbin.org/get")
>>> r = requests.options("http://httpbin.org/get")

如果要使用get方式来获得某一个参数
Requests 允许使用 params 关键字参数，以一个字符串字典来提供这些参数。举例来说，如果你想传递 key1=value1 和 key2=value2 到 httpbin.org/get ，那么你可以使用如下代码：
>>> payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.get("http://httpbin.org/get", params=payload)
通过打印输出该 URL，你能看到 URL 已被正确编码：
>>> print(r.url)
http://httpbin.org/get?key2=value2&key1=value1
注意字典里值为 None 的键都不会被添加到 URL 的查询字符串里。
你还可以将一个列表作为值传入：
>>> payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

>>> r = requests.get('http://httpbin.org/get', params=payload)
>>> print(r.url)
http://httpbin.org/get?key1=value1&key2=value2&key2=value3

响应内容
>>> import requests
>>> r = requests.get('https://github.com/timeline.json')
>>> r.text
u'[{"repository":{"open_issues":0,"url":"https://github.com/...
Requests 会自动解码来自服务器的内容，而且还可以自己推测是什么编码。你可以输入encoding查看是什么编码，也可以改变这个对象r的编码方式：
>>> r.encoding
'utf-8'
>>> r.encoding = 'ISO-8859-1'

二进制响应内容
你也能以字节的方式访问请求响应体，对于非文本请求：
>>> r.content
b'[{"repository":{"open_issues":0,"url":"https://github.com/...
Requests 会自动为你解码 gzip 和 deflate 传输编码的响应数据。
例如，以请求返回的二进制数据创建一张图片，你可以使用如下代码：
>>> from PIL import Image
>>> from io import BytesIO

>>> i = Image.open(BytesIO(r.content))


JSON 响应内容
Requests 中也有一个内置的 JSON 解码器：
>>> import requests

>>> r = requests.get('https://github.com/timeline.json')
>>> r.json()
[{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...
如果 JSON 解码失败， r.json() 就会抛出一个异常。例如，响应内容是 401 (Unauthorized)，尝试访问 r.json() 将会抛出 ValueError: No JSON object could be decoded 异常。
需要注意的是，成功调用 r.json() 并**不**意味着响应的成功。有的服务器会在失败的响应中包含一个 JSON 对象（比如 HTTP 500 的错误细节）。这种 JSON 会被解码返回。要检查请求是否成功，请使用 r.raise_for_status() 或者检查 r.status_code 是否和你的期望相同。

个人定制你的headers
	如果在get请求的时候要构建一个special header，你只需要用一个字典来传入信息就可以了。
>>> url = 'https://api.github.com/some/endpoint'
>>> headers = {'user-agent': 'my-app/0.0.1'}
>>> r = requests.get(url, headers=headers)
注意: 定制 header 的优先级低于某些特定的信息源，例如：
	•	在 .netrc 中设置了用户认证信息，使用 headers= 设置的授权就不会生效。而如果设置了 auth= 参数，``.netrc`` 的设置就无效了。
	•	如果被重定向到别的主机，授权 header 就会被删除。
	•	代理授权 header 会被 URL 中提供的代理身份覆盖掉。
	•	在我们能判断内容长度的情况下，header 的 Content-Length 会被改写。
	更进一步讲，Requests 不会基于定制 header 的具体情况改变自己的行为。只不过在最后的请求中，所有的 header 信息都会被传递进去。
注意: 所有的 header 值必须是 string、bytestring 或者 unicode。尽管传递 unicode header 也是允许的，但不建议这样做。

更加复杂的 POST 请求
如果你想要发送一些编码为表单形式的数据（像一个真正的HTML 表单内种的话）传递一个字典给 data 参数就可以惹。发出请求时会自动编码为表单形式：
>>> payload = {'key1': 'value1', 'key2': 'value2'}

>>> r = requests.post("http://httpbin.org/post", data=payload)
>>> print(r.text)
{
  ...
  "form": {
    "key2": "value2",
    "key1": "value1"
  },
  ...
}
还可以为 data 参数传入一个元组列表。在表单中多个元素使用同一 key 的时候，这种方式就显得比较有效：
>>> payload = (('key1', 'value1'), ('key1', 'value2'))
>>> r = requests.post('http://httpbin.org/post', data=payload)
>>> print(r.text)
{
  ...
  "form": {
    "key1": [
      "value1",
      "value2"
    ]
  },
  ...
}
如果你要发送的数据不需要以表单形式编码，输入一个string 那么数据就会被直接发布出去。
例如，Github API v3 接受编码为 JSON 的 POST/PATCH 数据：
>>> import json

>>> url = 'https://api.github.com/some/endpoint'
>>> payload = {'some': 'data'}

>>> r = requests.post(url, data=json.dumps(payload))
此处除了可以自行对 dict 进行编码，你还可以使用 json 参数直接传递，然后它就会被自动编码。这是 2.4.2 版的新加功能：
>>> url = 'https://api.github.com/some/endpoint'
>>> payload = {'some': 'data'}

>>> r = requests.post(url, json=payload)


响应状态码
我们可以这样检测响应状态码：
>>> r = requests.get('http://httpbin.org/get')
>>> r.status_code
200
为方便引用，Requests还附带了一个内置的状态码查询对象：
>>> r.status_code == requests.codes.ok
True
如果发送了一个错误请求(一个 4XX 客户端错误，或者 5XX 服务器错误响应)，我们可以通过raise_for_status()来抛出异常：
>>> bad_r = requests.get('http://httpbin.org/status/404')
>>> bad_r.status_code
404

>>> bad_r.raise_for_status()
Traceback (most recent call last):
  File "requests/models.py", line 832, in raise_for_status
    raise http_error
requests.exceptions.HTTPError: 404 Client Error
但是，由于我们的例子中 r 的 status_code 是 200 ，当我们调用 raise_for_status() 时，得到的是：
>>> r.raise_for_status()
None
一切都挺和谐哈。



cookies 参数：
>>> url = 'http://httpbin.org/cookies'
>>> cookies = dict(cookies_are='working')

>>> r = requests.get(url, cookies=cookies)
>>> r.text
'{"cookies": {"cookies_are": "working"}}'


超时
你可以告诉 requests 在经过以 timeout 参数设定的秒数时间之后停止等待响应。基本上所有的代码都应该使用这一参数。如果不使用，你的程序可能会永远失去响应：
>>> requests.get('http://github.com', timeout=0.001)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
requests.exceptions.Timeout: HTTPConnectionPool(host='github.com', port=80): Request timed out. (timeout=0.001)
注意
timeout 仅对连接过程有效，与响应体的下载无关。 也就是说这个时间内没有获取任何内容的时候停止响应，而不是没有下载完的时候停止响应。

