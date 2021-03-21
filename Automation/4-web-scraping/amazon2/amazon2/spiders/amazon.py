import scrapy
from ..items import Amazon2Item

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/s?k=books&rh=n%3A283155%2Cn%3A17&dc&qid=1616345019&rnid=2941120011&ref=sr_nr_n_2',
    "https://www.amazon.com/s?k=books&i=stripbooks&rh=n%3A283155%2Cn%3A4736&dc&qid=1616345263&rnid=283155&ref=sr_nr_n_1",
    "https://www.amazon.com/s?k=books&i=stripbooks&rh=n%3A283155%2Cn%3A2&dc&qid=1616345263&rnid=283155&ref=sr_nr_n_2",
    "https://www.amazon.com/s?k=books&i=stripbooks&rh=n%3A283155%2Cn%3A12290&dc&qid=1616345263&rnid=283155&ref=sr_nr_n_3",
    "https://www.amazon.com/s?k=books&i=stripbooks&rh=n%3A283155%2Cn%3A6&dc&qid=1616345263&rnid=283155&ref=sr_nr_n_6",
    "https://www.amazon.com/s?k=books&i=stripbooks&rh=n%3A283155%2Cn%3A9&dc&qid=1616345263&rnid=283155&ref=sr_nr_n_7"]

    def parse(self, response):
        book = Amazon2Item()

        for item in response.css(".s-asin .sg-col-inner"):
            
            title = item.css("span.a-size-base-plus::text").extract()
            if title:
                book["title"] = str(title)

            rating = item.css("div.a-row.a-size-small > span::attr(aria-label)").extract()
            if rating is not None and len(rating) > 0:
                book["rating"] = rating[0]

            price = item.css("span.a-price span.a-offscreen::text").extract()
            if price:
                book["price"] = price[0]

            yield book
        
        pages = response.css(".a-pagination > .a-last > a::attr(href)").extract()
        for next_page in pages:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)          
    

