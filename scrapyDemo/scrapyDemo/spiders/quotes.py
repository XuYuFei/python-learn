import scrapy
from scrapy.crawler import CrawlerProcess               # 导入CrawlerProcess类
from scrapy.utils.project import get_project_settings   # 导入获取项目设置信息

from scrapyDemo.items import ScrapydemoItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'

    def start_requests(self):
        # 设置爬取目标的地址
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/'
        ]

        # 获取所有地址，有几个地址发送几次请求
        for url in urls:
            # 发送网络请求
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        # CSS提取数据
        title = response.css('title').extract()
        text = response.css('title::text').extract_first()
        print(dict(title = title, text = text))

        # XPath提取数据
        # 获取所有信息
        for quote in response.xpath(".//*[@class='quote']"):
            # 获取名人名言文字信息
            text = quote.xpath(".//*[@class='text']/text()").extract_first()
            # 获取作者
            author = quote.xpath(".//*[@class='author']/text()").extract_first()
            # 获取标签
            tags = quote.xpath(".//*[@class='tag']/text()").extract()

            # 创建Item对象
            item = ScrapydemoItem(text = text, author = author, tags = tags)
            yield item # 输出信息

            # 以字典形式输出信息
            print(dict(text=text, author = author, tags = tags))

        # 实现翻页
        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, self.parse())

        # 获取网页
        page = response.url.split('/')[-2]
        # 根据页数设置文件名称
        filename = 'quotes-%s.html' % page
        # 写入文件的模式打开文件，如果没有该文件将创建该文件
        with open(filename, 'wb') as f:
            # 向文件中写入获取的html代码
            f.write(response.body)
        self.log('Saved file %s' % filename)

# 程序入口
if __name__ == '__main__':
    # 创建CrawlerProcess类对象并传入项目设置信息参数
    process = CrawlerProcess(get_project_settings())
    # 设置需要启动的爬虫名称
    process.crawl('quotes')
    # 启动爬虫
    process.start()