# -*- coding: utf-8 -*-
import requests
import os
from bs4 import BeautifulSoup as bs
""""
r.status_code #状态 200正常
r.text #字符串
r.encoding #从HTTP header中猜测的相应内容编码方式
r.apparent_encoding  从内容中分析（也是猜测）出的响应内容编码方式（备选编码方式）
r.content #二进制（如图片）
"""
# url = "https://www.amazon.cn/dp/B078FFX8B6/ref=cngwdyfloorv2_recs_0/462-1662042-7399636?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-2&pf_rd_r=E02KDWK3QC97M9DWRC9A&pf_rd_r=E02KDWK3QC97M9DWRC9A&pf_rd_t=36701&pf_rd_p=7149a3bb-2ee6-4f99-92eb-d87852365f8c&pf_rd_p=7149a3bb-2ee6-4f99-92eb-d87852365f8c&pf_rd_i=desktop"
# url = "https://baidu.com"
# r = requests.get(url)
# print(type(r))
# print(r.status_code)
# print(r.request.headers)
# print(r.headers)    # response
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
        cookies: 字典或CookieJar，Request中的cookie
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
# fs = {'file': open('data.xls', 'rb')}
# r = requests.request('POST', "http://python123.io/ws", files=fs, timeout=10)
# pxs = {'http': 'http://user:pass@10.10.10.1:1234', 'https': 'https://10.10.10.1:4321'}
# r = requests.request('GET', 'http://www.baidu.com', proxies=pxs)
# # 常用的放到函数设计里面，不常用的放到可选的参数里面
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

# 亚马逊
# url = "https://www.amazon.cn/dp/B078FFX8B6/ref=cngwdyfloorv2_recs_0/462-1662042-7399636?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-2&pf_rd_r=E02KDWK3QC97M9DWRC9A&pf_rd_r=E02KDWK3QC97M9DWRC9A&pf_rd_t=36701&pf_rd_p=7149a3bb-2ee6-4f99-92eb-d87852365f8c&pf_rd_p=7149a3bb-2ee6-4f99-92eb-d87852365f8c&pf_rd_i=desktop"
# kv = {'user-agent': 'Mozilla/5.0'}
# r = requests.get(url, headers=kv)
# # print(type(r))
# print(r.status_code)
# print(r.request.headers)
# print(r.headers)    # response
# r.encoding = r.apparent_encoding
# print(r.encoding)
# print(r.apparent_encoding)
# print(r.text)

# kv = {'wd': 'Python'}
# url = "https://baidu.com/s"
# r = requests.get(url, params=kv)
# print(r.status_code)
# print(r.request.url)
# print(len(r.text))

# url = "https://www.so.com/s"
# keyword = 'Python'
# try:
#     kv = {'q': keyword}
#     r = requests.get(url, params=kv)
#     print(r.request.url)
#     print(r.raise_for_status())
#     print(len(r.text))
# except:
#     print("爬取失败")

# path = "D:/ab.jpg"
# url = "http://image.ngchina.com.cn/2017/0411/20170411122223468.jpg"
# r = requests.get(url)
# print(r.status_code)
# # print(r.raise_for_status())
# with open(path, 'wb') as f:
#     f.write(r.content)

# url = "http://image.ngchina.com.cn/2017/0411/20170411122223468.jpg"
# root = "C:/image/"
# path = root + url.split('/')[-1]
# try:
#     if not os.path.exists(root):
#         os.mkdir(root)
#     if not os.path.exists(path):
#         r = requests.get(url)
#         with open(path, 'wb') as f:
#             f.write(r.content)
#             f.close()
#             print("文件保存成功")
#     else:
#         print("文件已存在")
# except:
#     print("爬取失败")

# url = "http://ip138.com/ips138.asp?ip="
# r = requests.get(url + '202.204.80.112')
# try:
#     print(r.encoding)
#     print(r.apparent_encoding)
#     r.encoding = r.apparent_encoding
#     print(r.status_code)
#     print(r.text[-500:]) # 若数据太多，可能会失效
# except:
#     print("爬取失败")

"""
BS 解析器
BeautifulSoup(mk,'html.parser')
BeautifulSoup(mk,'lxml')
BeautifulSoup(mk,'xml')
BeautifulSoup(mk,'html5lib')
"""

"""
BS 类的基本元素
Tag 标签，最基本的信息组织单元，分别用<>和</>表明开头和结尾
Name 标签的名字，<p>...</p>的名字是'p',格式：<tag>.name
Attributes 属性，字典形式组织，格式：<tag>.attrs
NavigableString 非属性字符串，<>...</>中字符串，格式：<tag>.string
Comment 字符串的注释部分，一种特殊的Comment类型
"""

url = "https://python123.io/ws/demo.html"
r = requests.get(url)
print(r.status_code)
# 抛出的异常
print(r.raise_for_status())
demo = r.text
# print(demo)
# 解析器
soup = bs(demo, 'html.parser')
# print(soup.prettify())
print(soup.title)
# 只能获得第一个
tag = soup.a
print(tag)
print(tag.attrs)
print(type(tag.attrs))
print(tag.attrs['href'])
print(type(tag))
print(soup.a.string)
print(type(soup.p.string))