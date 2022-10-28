import scrapy


class QuotesSpider(scrapy.Spider):
    name = "toscrape-xpath"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        
        
        quotes = response.xpath('//div[@class="quote"]')[0].xpath('//span[@class="text"]/text()').getall()
        authors = response.xpath('//div[@class="quote"]')[0].xpath('//small[@class="author"]/text()').getall()
        tags = response.xpath('//div[(@class="quote")]')[0].xpath('//a[@class="tag"]/text()').getall()
	
        for i in range(len(quotes)):
            yield {
                'text': quotes[i],
                'author': authors[i],
                'tags': authors[i],
            }

        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield response.follow(next_page, callback=self.parse)
