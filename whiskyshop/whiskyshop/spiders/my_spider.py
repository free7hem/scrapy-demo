import scrapy
import uuid


class MySpiderSpider(scrapy.Spider):
    name = 'my-spider'
    allowed_domains = ['www.whiskyshop.com']
    start_urls = ['https://www.whiskyshop.com/single-malt-scotch-whisky']

    def parse(self, response):
        products = response.css('div.product-item-info')
        
        for product in products:
            try: 
                img = product.css('img.product-image-photo').attrib['src']
            except:
                img = ''
            
            price = product.css('span.price::text').get()
            price = price.replace('£','') if price is not None else 0.0
            yield {
                'name': product.css('a.product-item-link::text').get(),
                'price': price,
                'link': product.css('a.product-item-link').attrib['href'],
                'img': img,
                'id': str(uuid.uuid4())
            }
        
        next_page = response.css('a.next.action').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)
