from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = "carbon"
    allowed_domains = ["https://www.carbon38.com/"]
    start_urls = ["https://carbon38.com/collections/tops?filter.p.m.custom.available_or_waitlist=1"]
    #
    # rules = (
    #     Rule(LinkExtractor(allow="catalogue/category")),
    #     Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item")
    # )
    #
    #
    #
    #
    # def parse_item(self,response):
    #  yield {
    #     "title": response.css(".ProductMeta h2::text").get(),
    #     "price":response.css(".ProductMeta__PriceList Heading span.ProductMeta__Price Price::text").get(),
    #     }




    def parse(self,response):
        for products in response.css('div.ProductItem__Info'):
            yield {

                "name" : products.css("h2.ProductItem__Title a::text").get(),
                "price" : products.css("span.ProductItem__Price").get().replace('<span class="ProductItem__Price Price">','').replace('</span>',''),
                "url" : products.css('h2.ProductItem__Title a').attrib['href'],


            }


