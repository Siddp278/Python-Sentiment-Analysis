# -*- coding: utf-8 -*-
import scrapy
from ..items import ImbdItem

class ReviewSpider(scrapy.Spider):
    name = 'review'
    start_urls = ['https://www.imdb.com/title/tt0903747/']
    links = ['/title/tt0903747/','/title/tt1520211/','/title/tt1475582/','/title/tt0108778/',
               '/title/tt4574334/','/title/tt0898266/','/title/tt0460649/','/title/tt0411008/','/title/tt2356777/',
               '/title/tt0455275/','/title/tt7366338/','/title/tt2193021/','/title/tt0412142/','/title/tt2085059/',
               '/title/tt0475784/', '/title/tt2306299/','/title/tt0460681/','/title/tt0386676/','/title/tt0096697/',
               '/title/tt1632701/','/title/tt2861424/', '/title/tt2707408/', '/title/tt1442437/',
               '/title/tt4158110/', '/title/tt2802850/', '/title/tt1796960/', '/title/tt3107288/', '/title/tt3032476/',
               '/title/tt2442560/', '/title/tt0141842/', '/title/tt1405406/','/title/tt0306414/',
               '/title/tt1844624/',
               '/title/tt5180504/',
               '/title/tt1124373/',
               '/title/tt0413573/',
               '/title/tt6468322/',
               '/title/tt1266020/',
               '/title/tt0804503/',
               '/title/tt2661044/',
               '/title/tt4052886/',
               '/title/tt2467372/',
               '/title/tt1586680/',
               '/title/tt1439629/',
               '/title/tt2741602/',
               '/title/tt5753856/',
               '/title/tt8111088/',
               '/title/tt5834204/',
               '/title/tt0452046/',
               '/title/tt5071412/',
               '/title/tt1190634/',
               '/title/tt3920596/',
               '/title/tt2261227/',
               '/title/tt7767422/',
               '/title/tt7335184/',
               '/title/tt0364845/',
               '/title/tt3205802/',
               '/title/tt4786824/',
               '/title/tt3006802/',
               '/title/tt5420376/',
               '/title/tt5555260/',
               '/title/tt0491738/',
               '/title/tt0203259/',
               '/title/tt7016936/',
               '/title/tt4179452/',
               '/title/tt6470478/',
               '/title/tt0458290/',
               '/title/tt8550800/',
               '/title/tt11823076/',
               '/title/tt3502248/',
               '/title/tt7134908/',
               '/title/tt2261391/',
               '/title/tt8806524/',
               '/title/tt3526078/',
               '/title/tt3007572/',
               '/title/tt7660850/',
               '/title/tt2805096/',
               '/title/tt9815454/',
               '/title/tt7456722/',
               '/title/tt7908628/',
               '/title/tt7008682/',
               '/title/tt7587890/',
               '/title/tt8103070/',
               '/title/tt7817340/',
               '/title/tt12004706/',
               '/title/tt4524056/',
               '/title/tt8134186/',
               '/title/tt8741290/',
               '/title/tt7414406/',
               '/title/tt8089592/',
               '/title/tt10293938/',
               '/title/tt6874964/',
               '/title/tt10228230/',
               '/title/tt10726356/',
               '/title/tt8045468/',
               '/title/tt9059820/',
               '/title/tt9642982/',
               '/title/tt9244556/',
               '/title/tt10098482/']

    def parse(self, response):
        items = ImbdItem()
        i = 0
        while i < len(ReviewSpider.links):
            use_url = ''
            if i < len(ReviewSpider.links):
                i = i + 1
                use_url = 'https://www.imdb.com' + str(ReviewSpider.links[i])
                title = response.css('h1::text').extract()
                rating = response.xpath('//strong//span/text()').extract()
                storyline = response.xpath('//p//span/text()').extract()
                genre = response.css('.txt-block~ .canwrap a::text').extract()

                items['title'] = title
                items['rating'] = rating
                items['storyline'] = storyline
                items['genre'] = genre
                yield items
                yield response.follow(use_url, callback=self.parse)


#DOWNLOADER_MIDDLEWARES = {
    # ...
    #'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
    #'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
    # ...
#}
#copy paste it in settings without the comments.