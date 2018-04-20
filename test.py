# -*- coding: utf-8 -*-
import requests
import os
import re
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

# url = "https://python123.io/ws/demo.html"
# r = requests.get(url)
# print(r.status_code)
# # 抛出的异常
# print(r.raise_for_status())
# demo = r.text
# print(demo)
# 解析器
# soup = bs(demo, 'html.parser')
# print(soup.prettify())
# print(soup.title)
# print(soup.a)
# print(soup.a.parent)
# print(soup.a.parent.parent)
# 只能获得第一个
# tag = soup.a
# print(tag)
"""
标签树的下行遍历
.contents 子节点的列表，将<tag>所有儿子节点存入列表
.children 子节点的迭代类型，与.contents类似，用于循环遍历
.descendants 子孙节点的迭代类型，包含所有子孙节点，用于循环遍历
"""

# url = "https://python123.io/ws/demo.html"
# r = requests.get(url)
# demo = r.text
# soup = bs(demo, "html.parser")
# print(soup.head)
# print(soup.head.contents)
# print(soup.body.contents)
# print(len(soup.body.contents))
# # print(soup.body.contents[1])
# for child in soup.body.contents:
#     print(child)
# for child in soup.body.children:
#     print(child)

"""
标签树的上行遍历
.parent 节点的父亲比标签
.parents  节点先辈标签的迭代类型，用于循环遍历先辈节点
"""
# url = "https://python123.io/ws/demo.html"
# r = requests.get(url)
# demo = r.text
# soup = bs(demo, "html.parser")
# # print(soup.title.parent)
# # print(soup.html.parent) # html是最高级标签，本身
# # print(soup.parent)
# for parent in soup.a.parents:
#     if parent is None:
#         print(parent)
#     else:
#         print(parent.name)

"""
平行遍历
.next_sibling 返回按照HTML文本顺序的下一个平行节点标签
.previous_sibling 返回按照HTML文本顺序的上一个平行节点标签
.next_siblings 迭代类型，返回按照HTML文本顺序的后续所有平行节点标签
.previous_siblings 迭代类型，返回按照HTML文本顺序的前续所有平行节点标签
注意：平行遍历发生在同一个父亲节点下
"""

# soup = bs(demo, 'html.parser')
# print(soup)
# print(soup.a.next_sibling)
# print(soup.a.next_sibling.next_sibling)
# print(soup.a.previous_sibling)
# print(soup.a.previous_sibling.previous_sibling)
# for sibling in soup.a.next_siblings:
#     print(sibling)

# url = "https://python123.io/ws/demo.html"
# r = requests.get(url)
# demo = r.text
# soup = bs(demo, 'html.parser')
# print(soup.prettify())
# print(soup)
# print(soup.a.prettify())
"""
信息标记和提取方法
XML <>..</> or < />, 最早的通用信息标记语言，可扩展性好，但繁琐。Internet上的信息交互与传递
JSON 信息有类型 key: value，适合程序处理（js），较XML简洁。移动应用云端和节点的信息通信，无注释
YAML 信息无类型 key: value，文本信息比例最高，可读性好。各类系统的配置文件，有注释易读
"""

"""
形式解析和搜索方法
提取HTML中所有URL链接
1）搜索到所有<a>标签
2）解析<a>标签格式，提取href后的链接内容
"""
url = "https://python123.io/ws/demo.html"
r = requests.get(url)
demo = r.text
soup = bs(demo, 'html.parser')
# for link in soup.find_all('a'):
#     print(link.get('href'))

"""
<>.find_all(name, attrs, recursive, string **kwargs)
返回一个列表类型，存储查找的结果
name：对标签名称的检索字符串
atrrs: 对标签属性值的检索字符串，可标注属性检索
recursive:Bool类型，是否对子孙全部检索，默认True
string: <>...</>中字符串区域的检索字符串
注:
    <tag>(..) 等价于 <tag>.find_all(..)
    soup(..) 等价于 soup.find_all(..) 
"""
# for tag in soup.find_all(re.compile('b')):
#     print(tag.name)

# print(soup.find_all('p', 'course'))
# print(soup.find_all(id='link1'))
# print(soup.find_all(id=re.compile('link')))
print(soup.find_all('a'))
print(soup('a'))
print(soup.find_all('a', recursive=False)) # soup的儿子层面没有"a"标签
print(soup('a', recursive=False))
# print(soup.find_all(string="Basic Python"))
print(soup.find_all(string=re.compile('Python')))

"""
一下方法的参数同.find_all()参数
<>.find() 搜索返回一个结果，字符串类型
<>.find_parents 在先辈中搜索，返回列表类型
<>.find_parent 在先辈中搜索一个，返回字符串
<>.find_next_siblings() 在后序平行节点中搜索，返回列表
<>.find_next_sibling() 在后序平行节点中搜索一个，返回字符串
<>.find_previous_sibling() 在前序平行节点中搜索一个，返回字符串
<>.find_previous_siblings() 在前序平行节点中搜索，返回列表
"""