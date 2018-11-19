import scrapy
import pprint 
import sys
from clx.items import LinksItem
# global variable
visited_urls = dict()
captured_urls = dict()
cap= 0
cnt = 0
class LinksSpider(scrapy.Spider):
    '''spider name'''
    name = "links"
    def start_requests(self):
        global visited_urls
        global cap
        self.url = getattr(self, 'url', 'https://quotes.toscrape.com/page/1/')
        self.k   = int(getattr(self, 'k', 100))
        cap = self.k
        visited_urls[self.url] = True
        captured_urls[self.url] = True
        print(f'k = {self.k}')
        print(f'processing {self.url}')
        yield scrapy.Request(url=self.url, callback=self.parseGetAllLinks)
    
    '''
    for sel in contents[:k]:
    # .re(r'.*product.*|.*business.*|.*services.*|.*stores.*|.*projects.*')
    item = LinksItem()
    item['name'] = sel.xpath('text()').extract()
    item['link'] = sel.xpath('@href').extract()
    yield item
    '''
    def parseGetAllLinks(self, response):
        global visited_urls
        global captured_urls
        global cap
        global cnt
        urls_in_page = response.css("a::attr(href)").extract()
        next_urls = []
        
        pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(urls_in_page)
        
        for post_url in urls_in_page:
            post_url = response.urljoin(post_url)
            if post_url in visited_urls:
                continue 
            if post_url in captured_urls:
                continue
            next_urls.append(post_url)
        
        bkp_next_url = ""
        for idx in range(len(next_urls)): 
            # print cnt
            if next_urls[idx] in captured_urls:
                continue
            else:
                captured_urls[next_urls[idx]] = True
                bkp_next_url = next_urls[idx]
            if cnt == cap:
                print("reach the end")
                break
                sys.exit(0)
            cnt += 1
            item = LinksItem()
            item['name'] = cnt
            item['link'] = next_urls[idx]
            yield item
        if cnt < cap:
            print(f'go to next url: {bkp_next_url}')
            yield scrapy.Request(url = bkp_next_url, callback=self.parseGetAllLinks)
        else:
            print(f'get all {cnt} pages')


    '''different parsers'''
    def getLinks(self, response):
        print("Processing..." + response.url)
        k = self.k
        pat = '.*'#'product|business|service|store|project|content|shop'
        contents = response.xpath("//a[re:test(@href, $val)]", val = pat) # //div/ul/li/a[re:test(@href, $val)]
        # print contents
        if len(contents) == 0:
            yield response.url
        else:
            for sel in contents[:k]:
                # .re(r'.*product.*|.*business.*|.*services.*|.*stores.*|.*projects.*')
                item = LinksItem()
                item['name'] = sel.xpath('text()').extract()
                item['link'] = sel.xpath('@href').extract()
                yield item

    
    '''
    Scrapy schedules the scrapy.Request objects returned by the start_requests method of the Spider.
    Upon receiving a response for each one, it instantiates Response objects and calls the callback method associated with the request 
    (in this case, the parse method) passing the response as argument.
    eg:
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]'''

    def parse(self, response):
        print("Processing..." + response.url)
        # page = response.url.split("/")[-2]
        filename = 'urls.txt' #% str(response.url).split("\\.")[0]
        with open(filename, 'a') as f:
            f.write(response.url + '\n')
        self.log('Saved file %s' % filename)

    def parseNextLink(self, response):
        urls_in_page = response.css("li.next a::attr(href)").extract_first()
        if urls_in_page is not None:
            urls_in_page = response.urljoin(next_page)
            yield next_page
            # yield scrapy.Request(next_page, callback = self.parse)
    
    def parseItem(self, response):
        for q in response.css('div.quote'):
            yield {
                'text': q.css('span.text::text').extract_first(),
                'author': q.css('small.author::text').extract_first(),
                'tag': q.css('div.tags a.tag::text').extract(),
            }
