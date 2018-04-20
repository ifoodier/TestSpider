# -*- coding: utf-8 -*-
import requests
import bs4
from bs4 import BeautifulSoup as bs


"""
程序结构设计：
步骤一：从网络获取大学排名网页内容
    getHTMLText()
步骤二：提取网页内容中信息到合适的数据结构
    fillUnivList()
步骤三：利用数据结构展示并输出结果
    printUnivList()
"""

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()    # 产生异常信息
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

    # r = requests.get(url)
    # demo = r.text
    # print(r.encoding)
    # print(r.apparent_encoding)
    # r.encoding = r.apparent_encoding
    # soup = bs(demo, 'html.parser')
    # print(soup.find_all('tr'))
    # for uni in soup.find_all(_class='alt'):
    #     print(uni)

    return ""

def fillUnivList(ulist, html):
    soup = bs(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')  # tds = tr.find_all('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string])

def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名", "学校名称", "省市", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288))) #chr(12288)中文字符空格

def main():
    uinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)

main()


