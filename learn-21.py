# *_* code: UTF-8 *_*
# author:   Beiyu
# datetime: 2019-12-28 14:10
# filename: learn-21.PY
# tool:     PyCharm
""" 21 - 网络爬虫框架 """

# 21.1 - 初识网络爬虫
# 21.1.1 - 网络爬虫概述
# 21.1.2 - 网络爬虫的分类
"""
    网络爬虫按照实现的技术和结构可以分为以下几种类型：
        - 通用网络爬虫
        - 聚焦网络爬虫
        - 增量式网络爬虫
        - 深层网络爬虫
        ......
"""

# 21.1.3 - 网络爬虫的基本原理
"""
    网络爬虫的基本工作流程：
    1、获取初始的URL，该URL地址是用户自己制定的初始爬取的网页；
    2、爬取对应URL地址的网页时，获取新的URL地址；
    3、将新的URL地址放入URL队列中；
    4、从URL队列中读取新的URL，然后依据新的URL爬取网页，同时从新的网页中获取新的URL地址，重复上述的爬取过程；
    5、设置停止条件；
"""

# 21.2 - 网络爬虫的常用技术

# 21.2.1 - Python的网络请求
"""
    Python中实现HTTP网络请求常见的三种方式：urllib、urllib3、requests
"""

# 21.2.1 - 1 - urllib模块
"""
    urllib提供了多个子模块，名称与含义如下：
        - urllib.request：该模块定义了打开URL的方法和类；
        - urllib.error：该模块中主要包含 异常类，基本的异常类是URLError；
        - urllib.parse：该模块定义的功能分为两大类：URL解析和URL引用；
        - urllib.robotparser：该模块用于解析robots.txt文件
"""
"""
# 通过get请求方式获取百度网页内容
import urllib.request

response = urllib.request.urlopen('http://www.baidu.com')
html = response.read()
print(html)
"""

"""
# 通过使用urllib.request模块的post请求实现获取网页信息的内容
import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data = data)
html = response.read()
print(html)

"""

# 21.2.1 - 2 - urllib3模块
"""
    urllib3是一个功能强大、条理清晰、用于HTTP客户端的Python库。
    urllib3重要特性：
        - 线程安全
        - 连接池
        - 客户端SSL/TLS验证
        - 使用多部分编码上传文件
        - Helpers用于重试请求并处理HTTP重定向
        - 支持gzip和deflate编码
        - 支持HTTP和SOCKS代理
        - 100%的测试覆盖率
    安装：pip install urllib3
"""
"""
import urllib3
http = urllib3.PoolManager()                                # 创建PoolManager对象，用于处理与线程池的连接以及线程安全的所有细节
response = http.request('GET', 'http://www.baidu.com')      # 对需要爬取的网页发送请求
# print(response.data)                                        # 打印读取内容
print(response)
response = http.request('POST', 'http://httpbin.org/post', fields = {'word': 'hello'})
print(response)

"""

# 21.2.1 - 3 - requests模块
"""
    安装：pip install requests
    优点：实现HTTP请求时比urllib模块简化、操作更加人性化
    requests功能特性：
        - Keep-Alive & 连接池          - Unicode响应体
        - 国际化域名和URL               - HTTP(S)代理支持
        - 带持久Cookie的会话            - 文件分块上传
        - 浏览器式的SSL认证             - 流下载
        - 自动内容解码                  - 连接超时
        - 基本 / 摘要式的身份认证        - 分块请求
        - 优雅的key/value Cookie       - 支持.netrc
        - 自动解压
        
    其他请求方式：
        - requests.put(url, data)   # PUT请求
        - requests.delete(url)      # DELETE请求
        - requests.head()           # HEAD请求
        - requests.options()        # OPTIONS请求
        
"""
"""
import requests

# GET请求方式
response = requests.get('http://www.baidu.com')
print(response.status_code)                         # 打印状态吗
print(response.url)                                 # 打印请求url
print(response.headers)                             # 打印头部信息
print(response.cookies)                             # 打印cookie信息
print(response.text)                                # 以文本形式打印网页源码
print(response.content)                             # 以字节流形式打印网页源码

# POST请求方式
data = {'word': 'hello'}                                            # 表单参数
response = requests.post('http://httpbin.org/post', data = data)    # 对需要爬取的网页发送请求
print(response.content)
"""

"""
import requests

payload = {'key1': 'value1', 'key2': 'value2'}                          # 传递的参数
response = requests.get('http://httpbin.org/get', params = payload)
print(response.content)
"""


# 21.2.2 - 请求headers处理
"""
    模拟浏览器头部信息，解决反爬设置问题
"""
"""
import requests
url = 'https://www.baidu.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
response = requests.get(url, headers = headers)
print(response.content)
"""

# 21.2.3 - 网络超时
"""
import requests

# 循环发送50次请求
for a in range(1, 50):
    try:                                                                    # 捕获异常
        response = requests.get('https://www.google.com/', timeout = 0.5)   # 设置超时为0.5秒
        print(response.status_code)
    except Exception as e:
        print('异常' + str(e))
"""
"""
import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException

for a in range(1, 10):
    try:
        response = requests.get('https://www.google.com/', timeout = 0.5)
        print(response.status_code)
    except ReadTimeout:
        print('timeout')
    except HTTPError:
        print('httperror')
    except RequestException:
        print('request error')
"""

# 21.2.4 - 代理服务

"""
import requests

proxy = {'http': '183.148.153.200:8080', 'https': '183.148.153.200:8080'}
response = requests.get('https://www.baidu.com', proxies = proxy)
print(response.content)
"""


# 21.2.5 - HTML解析之BeautifulSoup

# 21.2.5 - 1 - BeautifulSoup的安装
"""
    先安装bs4：pip install bs4
    安装：pip install beautifulsoup4
    安装lxml：pip install lxml
    安装html5lib：pip install html5lib
"""

# 21.2.5 - 2 - BeautifulSoup的使用
from bs4 import BeautifulSoup

# 创建模拟HTML代码的字符串
html_doc = """                          
<html><head><title>Demo</title></head>
<body>hello world</body></html>
"""

soup = BeautifulSoup(html_doc, features="lxml") # 创建一个BeautifulSoup对象，获取页面正文
print(soup)                                     # 打印解析的HTML代码


soup = BeautifulSoup(open('index.html'), 'lxml')    # 创建BeautifulSoup对象打开需要解析html文件
print(soup.prettify())                              # 打印格式化后的代码


# 21.3 - 网络爬虫开发常用框架

# 21.3.1 - Scrapy爬虫框架
"""
    网址：https://scrapy.org
    开源框架
"""

# 21.3.2 - Crawley爬虫框架
# 网址：http://project.crawley-cloud.com

# 21.3.3 - PySpider爬虫框架
"""
    源码地址：https://github.com/binux/pyspider/releases
    开发文档：http://docs.pyspider.org/
"""

# 21.4 - Scrapy爬虫框架的使用

# 21.4.1 - 搭建Scrapy爬虫框架

# 21.4.1 - 1 - 安装Twisted模块
"""
    下载扩展包：https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
    安装：pip install Twisted-19.10.0-cp38-cp38-win_amd64.whl
"""

# 21.4.1 - 2 - 安装Scrapy框架
"""
    命令：pip install Scrapy
"""

# 21.4.1 - 3 - 安装pywin32模块
"""
    命令：pip install pywin32
"""
"""
    国内镜像过慢，安装时在后面加 -i 地址
    例：pip install pywin32 -i https://mirrors.aliyun.com/pypi/simple/
    参考网址：https://blog.csdn.net/sunny_happy08/article/details/83113692
"""

# 21.4.2 - 创建Scrapy项目
"""
    创建scrapyDemo项目：scrapy startProject scrapyDemo
"""

# 21.4.3 - 创建爬虫
"""
    见：scrapyDemo项目下 scrapyDemo/spiders/quotes.py
    命令：scrapy crawl quotes
"""

# 21.4.4 - 获取数据
"""
    Scrapy爬虫框架，可以通过特定的CSS或者XPath表达式来选择HTML文件中的某一处，并且提取出相应的数据。
"""

# 21.4.4 - 1 - CSS提取数据
"""
    使用CSS提取HTML文件中的某一处数据时，可以指定HTML文件中的标签名称；
    response.css('title').extract()
    response.css('title::text').extract_firsst() 或 response.css('title::text')[0].extract()
"""

# 21.4.4 - 2 - XPath提取数据
"""
    使用XPath表达式提取HTML文件中的某一处数据时，需要根据XPath表达式的语法规定来获取指定的数据信息；
    获取title标签内信息：
        - response.xpath('//title/text()').extract_first()
"""

# 21.4.4 - 3 - 翻页提取数据




