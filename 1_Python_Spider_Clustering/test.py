import urllib.request
import urllib.parse
values = {"username":'xxx',"password":'xx'}
data = urllib.parse.urlencode(values).encode(encoding='utf_8')
url = "https://www.baidu.com/"
request = urllib.request.Request(url,data)
response = urllib.request.urlopen(request)
print (response.read())