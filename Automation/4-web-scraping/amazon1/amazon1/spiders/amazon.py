import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?k=kindle']

    def parse(self, response):
        name = response.css('.a-size-medium::text').extract()
        rating = response.css('.a-icon-star-small > .a-icon-alt::text').extract()
        price = response.css('.a-price > .a-offscreen::text').extract()
        yield {'item-name': name, 'item-price': price, 'item-rating': rating}
