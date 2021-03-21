import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?k=kindle']

    def parse(self, response):
        for item in response.css('.sg-col-inner'):
            name = item.css('.a-size-medium::text').extract()
            rating = item.css('.a-icon-star-small > .a-icon-alt::text').extract()
            price = item.css('.a-price > .a-offscreen::text').extract()
            if len(name) != 0 and len(rating) != 0 and len(price) != 0:
                yield {'item-name': name, 'item-price': price, 'item-rating': rating}
