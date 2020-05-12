import scrapy
from ..items import ImbdItem

class ReviewsSpider(scrapy.Spider):
    name = 'reviews'
    start_urls = ['https://www.imdb.com/chart/tvmeter/?sort=nv,desc&mode=simple&page=1']

    def parse(self, response):
        items = ImbdItem()
        links = response.css('td.titleColumn a').xpath('@href').extract() 

        items['links'] = links
        yield items 
