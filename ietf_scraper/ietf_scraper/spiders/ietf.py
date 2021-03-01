import scrapy
import w3lib.html


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        # title = response.css('span.title::text').get('title') CSS Selector
        # title = response.xpath('//span[@class="title"]/text()').get() #xPath selector
        # return {"title": title}
        return{
            'number': response.xpath('//span[@class="rfc-no"]/text()').get(),
            'title': response.xpath('//meta[@name="DC.Title"]/@content').get(),
            'date': response.xpath('//span[@class="date"]/text()').get(),
            'description': response.xpath('//meta[@name="DC.Description.Abstract"]/@content').get(),
            'author':response.xpath('//span[@class="author-name"]/text()').get(),
            'company': response.xpath('//span[@class="author-company"]/text()').get(),
            'address': response.xpath('//span[@class="address"]/text()').get(),
            'text': w3lib.html.remove_tags(response.xpath('//div[@class="text"]').get())
            # 'headings': response.xpath().getall()
        }
