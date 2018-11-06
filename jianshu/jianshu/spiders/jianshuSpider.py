# coding:utf-8
import time
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
# 为什么不能导入JianshuItem
from jianshu.items import JianshuItem


class Jianshu(CrawlSpider):
    '''
    #要建立一个 Spider，你可以为 scrapy.spider.BaseSpider 创建一个子类，并确定三个主要的、强制的属性：    
    #name ：爬虫的识别名，它必须是唯一的，在不同的爬虫中你必须定义不同的名字.    
    #start_urls ：爬虫开始爬的一个 URL 列表。爬虫从这里开始抓取数据，所以，第一次下载的数据将会从这些 URLS 开始。其他子 URL 将会从这些起始 URL 中继承性生成。   
    #parse() ：爬虫的方法，调用时候传入从每一个 URL 传回的 Response 对象作为参数，response 将会是 parse 方法的唯一的一个参数,    
    #这个方法负责解析返回的数据、匹配抓取的数据(解析为 item )并跟踪更多的 URL。    
    '''
    # name = 'jianshu'
    # start_urls= ['http://www.jianshu.com']
    # url = 'http://www.jianshu.com'

    name = 'jianshu'
    start_urls = ['https://www.testwo.com']
    url = 'https://www.testwo.com/'


    def parse(self, response):
        item = JianshuItem()
        selector = Selector(response)

        # response就是返回的网页数据
        # 处理好的数据放在items中，在items.py设置好你要处理哪些数据字段，这里我们抓取文章标题，url，作者，阅读数，喜欢，打赏数
        # 解析处理数据的地方，用xpath解析处理数据
        # 简书不让爬
        # articles = selector.xpath('//ul[@class="note-list"]/li')
        # 试试CSDN博客页面
        # articles = selector.xpath('//ul[@id="feedlist_id"]/li')
        # 测试窝
        articles = selector.xpath('/html/body/div[1]/div/div[1]/div[2]/div')


        for article in articles:
            # 简书
            # title = article.xpath('/div/a/text()').extract()
            # url = article.xpath('/div/a/@href').extract()
            # author = article.xpath('/div/div/a/text()').extract()

            # CSDN
            # title = article.xpath('/div/div/h2/a/text()').extract()
            # url = article.xpath('/div/div/h2/a/@href').extract()
            # author = article.xpath('/div/dl/dd[4]/a/text()').extract()

            # 测试窝
            # 相对xpath千万不要以斜杠“/”开头，否则获取不到数据
            title = article.xpath('div[1]/div/h3/a/text()').extract()
            url = article.xpath('div/div/h3/a/@href').extract()
            # author = article.xpath('/div/dl/dd[4]/a/text()').extract()


            # #下载所有热门文章的缩略图，有些文章没有
            # try:
            #     image = article.xpath('/a/img/@src').extract()
            #     # urllib.urlretrieve(image[0], '/Users/apple/Documents/images/%s-%s.jpg' % (author[0], title[0]))
            # except:
            #     print 'NO IMG'


            # 喜欢数

            # 评论数


            item['title'] = title
            item['url'] = url
            # item['author'] = author

            yield item
