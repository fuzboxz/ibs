import scrapy
from ..items import Amazon1Item


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?k=kindle']

    def parse(self, response):

        items = Amazon1Item()

        for item in response.css('.sg-col-inner'):
            name = item.css('.a-size-medium::text').extract_first()
            rating = item.css('.a-icon-star-small > .a-icon-alt::text').extract_first()
            price = item.css('.a-price > .a-offscreen::text').extract_first()
            
            if name is not None and price is not None and rating is not None:
                if len(name) != 0 and len(rating) != 0 and len(price) != 0:
                    
                    items["name"] = name
                    items["price"] = price
                    items["rating"] = rating

                    yield items

                    '''
                    yield {
                        'name': name, 
                        'price': price[0], 
                        'rating': rating
                    }
                    '''
