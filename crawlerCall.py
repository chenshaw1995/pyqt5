import sys
import os
# from clx.clx.spiders import links_spider
def call():
    # os.remove()
    dirname = os.path.dirname(os.path.abspath(__file__) )

    rmcmd = 'rm ' + dirname + '/clx/clx/crawl_result.csv'
    print rmcmd
    os.system(rmcmd)
    
    os.chdir(dirname + '/clx/clx/')
    
    # print os.getcwd()
    outfile = 'crawl_result.csv'
    url = 'https://www.microsoft.com'
    k = 10
    # 'https://quotes.toscrape.com/page/1/'
    # cmd = 'scrapy crawl --nolog links -o crawl_res.csv' ok
    # cmd = 'scrapy crawl links -o %s -a url=%s' % (outfile, url)# ok
    # cmd = 'scrapy crawl links -o %s -a k=%s' % (outfile, k)# ok
    cmd = 'scrapy crawl links -o %s -a url=%s -a k=%s' % (outfile, url, k)
    print cmd
    os.system(cmd)



if __name__ == '__main__':
    call()