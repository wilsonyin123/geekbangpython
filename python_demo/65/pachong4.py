# get请求
import requests
url = 'http://httpbin.org/get'
data = {'key': 'value', 'abc': 'xyz'}
# .get是使用get方式请求url，字典类型的data不用进行额外处理
response = requests.get(url, data)
print(response.text)


# post请求
import requests
url = 'http://httpbin.org/post'
data = {'key': 'value', 'abc': 'xyz'}
# .post表示为post方法
response = requests.post(url, data)
# 返回类型为json格式
print(response.json())