import scrapy


class ApnewsSpider(scrapy.Spider):
    name = 'apnews'
    allowed_domains = ['www.apnews.com']
    start_urls = ['http://www.apnews.com/']

    def parse(self, response):
        pass
