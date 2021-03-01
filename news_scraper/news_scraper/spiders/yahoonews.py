import scrapy


class YahoonewsSpider(scrapy.Spider):
    name = 'yahoonews'
    allowed_domains = ['news.yahoo.com']
    start_urls = ['http://news.yahoo.com/']

    def parse(self, response):
        pass
