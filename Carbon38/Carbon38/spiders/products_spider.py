import scrapy


# from scrapy.spiders import CrawlSpider,Rule
# from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(scrapy.Spider):
    name = "products_spider"
    allowed_domains = ["https://www.carbon38.com/"]
    start_urls = ["https://carbon38.com/collections/tops?filter.p.m.custom.available_or_waitlist=1"]


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
            
            # relative_url=product.css('h2.ProductItem__Title a').attrib['href']
            # item_url = 'https://carbon38.com' + relative_url
            # yield response.follow(item_url,callback = self.parse_tem_page)



            yield {

                "name" : product.css("h2.ProductItem__Title a::text").get(),
                "price" : product.css("span.ProductItem__Price").get().replace('<span class="ProductItem__Price Price">','').replace('</span>',''),
                "url" : product.css('h2.ProductItem__Title a').attrib['href'],
            
            }                                                    
            
            next_page = response.css('[rel="next"] ::attr(href)').get()
           

            if next_page is not None:
                next_page_url = 'https://carbon38.com' + next_page
                yield response.follow(next_page_url,callback = self.parse)


    # def parse_item_page(self,response):
          #  c=response.css('div.shopify-section').get()
        

    #     # for c in col:
    #     #     relative_url=response.css('h2.ProductItem__Title a').attrib['href']
        
    #     yield {

    #             "name" : response.css('h1.ProductMeta__Title ::text').get(),
    #             "price" : response.css('div.ProductMeta__PriceList span.ProductMeta__Price::text').get(),
    #             "url" : response.css('h2.ProductMeta__Vendor a').attrib['href'] ,             
    #             "color": response.css('span.ProductForm__Label span.ProductForm__SelectedValue::text').get() ,   
    #         }
