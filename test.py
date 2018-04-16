# -*- coding: utf-8 -*-
import requests

""""
r.status_code #状态 200正常
r.text #字符串
r.encoding #从HTTP header中猜测的相应内容编码方式
r.apparent_encoding  从内容中分析（也是猜测）出的响应内容编码方式（备选编码方式）
r.content #二进制（如图片）
"""
# r = requests.get(url="http://baidu.com/")
# print(type(r))
# print(r.status_code)
# print(r.headers)
# r.encoding = r.apparent_encoding
# print(r.encoding)
# print(r.apparent_encoding)
# print(r.text)

"""
requests.ConnectionError #网络连接错误
requests.HTTPError #
requests.URLRequired #URL缺失
requests.TooManyRedirects
requests.ConnectionError #与远程服务器链接时间超出时间
requests.Timeout # 总共时间
"""
#
# def getHTMLText(url):
#     try:
#         r = requests.get(url, timeout=30)
#         r.raise_for_status() #如果不是200，引发HTTPError异常
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return "产生异常"
#
# if __name__ == "__main__":
#     url = "http://www.baidu.com"
#     print(getHTMLText(url))


"""
对应7个HTTP协议资源操作
requests.request()
requests.get()
requests.head()
requests.post() # 用于提交请求，可以更新或者创建资源，是非幂等的,多次执行，会创建多条记录
requests.put() # 用于向指定的URI传送更新资源，是幂等的
requests.patch()# 对put的补充，修改部分资源（局部更新）
requests.delete()
"""
# # 获取头部信息
# r = requests.head("http://httpbin.org/get")
# print(r.headers)
# print(r.text)

# # 向URL POST一个字典，自动编码为form表单
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post("http://httpbin.org/post", data = payload)
# print(r.text)

# # 想URL POST 一个字符串，自动编码为data
# r = requests.post("http://httpbin.org/post", data = 'ABC')
# print(r.text)

"""
requests.request(method, url, **kwargs)
    method: get/put/post等7种请求方式
    url: 拟获取网页rul链接
    **kwargs：控制访问的可选参数，共13个
        params：字典或字节序列，作为参数增加到url中
        data：字典、字节序列或文件对象，作为Request的内容
        json: JSON格式数据，作为Request的内容
        headers: 字典，HTTP定制头
        cookies: 字典或CokkieJar，Request中的cookie
        auth：元组，支持HTTP认证功能
        files：字典类型，传输文件
        timeout: 设置超时时间，单位秒
        proxies: 字典类型，设定访问代理服务器，可以增加登录认证
        
        allow_redirects: True/False，默认为True，重定向开关
        stream: True/False, 默认为True，获取内容立即下载开关
        verify: True/False， 默认为True，认证SSL证书开关
        cert: 本地SSL证书路径
"""

# kv = {'key1': 'value1', 'key2': 'value2'}
# r = requests.request("GET", "http://python123.io/ws", params=kv)
# print(r.url)
# # https://python123.io/ws?key1=value1&key2=value2
#
# kv = {'key1': 'value1', 'key2': 'value2'}
# r = requests.request("POST", "http://python123.io/ws", params=kv)
# print(r.url)
# # http://python123.io/ws?key1=value1&key2=value2
# body = '主体内容'
# r = requests.request("POST", "http://python123.io/ws", params=body)
# print(r.url)
# # http://python123.io/ws?%E4%B8%BB%E4%BD%93%E5%86%85%E5%AE%B9
fs = {'file': open('data.xls', 'rb')}
r = requests.request('POST', "http://python123.io/ws", files=fs, timeout=10)
pxs = {'http': 'http://user:pass@10.10.10.1:1234', 'https': 'https://10.10.10.1:4321'}
r = requests.request('GET', 'http://www.baidu.com', proxies=pxs)
# 常用的放到函数设计里面，不常用的放到可选的参数里面
"""
requests.get(url, params=None, **kwargs)
url: 拟获取网页rul链接
params：url中额外参数，字典或字节序列，可选
**kwargs: request方法中除了params的12个访问控制参数
"""
"""
request.head(url, **kwargs)
url: 拟获取页面url链接
**kwargs：13个控制访问的参数
"""
"""
request.post(url, data=None, json=None, **kwargs)
url: 拟更新页面url链接
data: 字典、字节序列或文件，Request的内容
json：JSON格式数据，Request的内容
**kwargs：11个控制访问的参数
"""
"""
request.put(url, data=None, **kwargs)
url: 拟更新页面url链接
data: 字典、字节序列或文件，Request的内容
**kwargs：12个控制访问的参数
"""
"""
request.patch(url, data=None, **kwargs)
url: 拟更新页面url链接
data: 字典、字节序列或文件，Request的内容
**kwargs：12个控制访问的参数
"""
"""
request.delete(url, data=None, **kwargs)
url: 拟删除页面url链接
**kwargs：13个控制访问的参数
"""