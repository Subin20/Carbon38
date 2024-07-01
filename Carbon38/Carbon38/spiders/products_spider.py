import scrapy


# from scrapy.spiders import CrawlSpider,Rule
# from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(scrapy.Spider):
    name = "products_spider"
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
         products = response.css('div.ProductItem__Info')
         for product in products:
            yield {

                "name" : product.css("h2.ProductItem__Title a::text").get(),
                "price" : product.css("span.ProductItem__Price").get().replace('<span class="ProductItem__Price Price">','').replace('</span>',''),
                "url" : product.css('h2.ProductItem__Title a').attrib['href'],


            }

            # next_page = response.css('[rel="next"] ::attr(href)').get()
            # if next_page is not None:
            #     next_page_url = 'https://carbon38.com/collections/tops?filter.p.m.custom.available_or_waitlist=1' + next_page
            #     yield response.follow(next_page_url,callback=self.parse)