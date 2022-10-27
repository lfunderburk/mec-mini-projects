import scrapy


class QuotesSpider(scrapy.Spider):
    name = "toscrape-xpath"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        
        yield {
            'text': response.xpath('//div[(@class="quote")]/span[@class="text"]/text()').get(),
            'author': response.xpath('//div[(@class="quote")]/small[@class="author"]/text()').get(),
            'tags': response.xpath('//div[(@class="quote")]/a[@class="tag"]/text()').getall(),
        }

        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield response.follow(next_page, callback=self.parse)
