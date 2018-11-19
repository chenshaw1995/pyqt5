import sys
import os
from pathlib import Path

def call(outfile = 'crawl_result.csv', url = 'https://quotes.toscrape.com/page/1/', k = 100):
    
    if url is None or len(url) == 0:
        print(f'invalid url: {url}')
        url = 'https://quotes.toscrape.com/page/1/'
        # sys.exit(0)

    dirname = os.path.dirname(os.path.abspath(__file__) )

    rm_file = os.path.join(dirname, 'clx/clx/crawl_result.csv') # f'{dirname}/clx/clx/crawl_result.csv'
    if os.path.isfile(rm_file):
        os.remove(rm_file)
    rm_file = os.path.join(dirname, 'NumericRecords.txt')#f'{dirname}/NumericRecords.txt'
    if os.path.isfile(rm_file):
        os.remove(rm_file)
    Path(rm_file).touch()
    if os.path.isfile(rm_file):
        print(f'{rm_file} is a empty file now')
    else:
        print(f'fail to create {rm_file}')
    os.chdir(os.path.join(dirname, 'clx/clx/')
    
    # print os.getcwd()
    
    # 'https://quotes.toscrape.com/page/1/'
    # cmd = 'scrapy crawl links -o crawl_result.csv'
    # cmd = 'scrapy crawl links -o %s -a url=%s' % (outfile, url)# ok
    # cmd = 'scrapy crawl links -o %s -a k=%s' % (outfile, k)# ok
    cmd = f'scrapy crawl links -o {outfile} -a url={url} -a k={k}'
    print(cmd)
    os.system(cmd)

if __name__ == '__main__':
    call()