
from __future__ import print_function
import sys
import random
import os

class URLs:

    def __init__(self):
        self.data_file = os.path.dirname(os.path.abspath(__file__)) + '/urlDictionary.data'
        self.crawl_result = os.path.dirname(os.path.abspath(__file__)) + '/clx/clx/crawl_result.csv'
        if not os.path.isfile(self.data_file):
            print('%s does not exist.' % self.data_file)
            self.createMap(self.data_file)
        else:
            urls = []
            with open(self.data_file, 'r') as f:
                for line in f.readlines():
                    tmp = line.split(' ')
                    urls.append(tmp[len(tmp) - 1])
            self.list = urls

    def initUrls(self):
        import csv
        urls = []
        
        with open(self.crawl_result) as f:
            csv_reader = csv.reader(f, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print ('Column names are %s' % (", ".join(row)) )
                    line_count += 1
                else:
                    print( row[0])
                    urls.append(row[0])
                    # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                    line_count += 1
            print('Processed %d lines.'% line_count)
              
        self.list = urls

    def createMap(self, fname):
        self.initUrls()

        with open(fname, 'w+') as f:
            for i in range(len(self.list)):
                row = '%s %s\n' % (i, self.list[i])
                f.write(row)

    def getList(self):
        return map(lambda x: x, self.list)
        # return self.list

    def iterator(self):
        self.id = 0
        self.it = iter(self.getList())
        return self.it

    def getNext(self):
        try:
            self.id += 1
            return next(self.it)
        except:
            return 'reach the end'
            # break


    def getRandomUrl(self):
        id = random.randint(0, len(self.list) - 1)
        
        return self.list[id]


def main():
    store = URLs()

    # myit = store.iterator()
    # for i in range(10):
    #     print(store.getNext())


    # us = ['https://microsoft.com', 'http://courses.cse.tamu.edu/caverlee/csce670/']
    # store = URLs(us)
    # # print('test list')
    # for e in store.list:
    #     print(e)
    # print('test random url')
    # print(store.getRandomUrl())


if __name__ == '__main__':
    main()