import scrapy


class CnnSpider(scrapy.Spider):
    name = 'cnn'
    allowed_domains = ['www.cnn.com']
    start_urls = ['http://www.cnn.com/']

    def parse(self, response):
        pass
