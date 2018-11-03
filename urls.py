
from __future__ import print_function
import sys
import random
import os

class URLs:

    def __init__(self):
        self.dataFile = os.path.dirname(os.path.abspath(__file__)) + '/urlDictionary.data'
        if not os.path.isfile(self.dataFile):
            print('%s does not exist.' % self.dataFile)
            self.createMap(self.dataFile)
        else:
            urls = []
            with open(self.dataFile, 'r') as f:
                for line in f.readlines():
                    tmp = line.split(' ')
                    urls.append(tmp[len(tmp) - 1])
            self.list = urls

    def initUrls(self):
        urls = []
        with open('products.txt', 'r') as f:
            for line in f.readlines():
                tmp = line.split(' ')
                urls.append(tmp[len(tmp) - 1])
        self.list = urls

    def createMap(self, fname):
        self.initUrls()

        with open(fname, 'w+') as f:
            for i in range(len(self.list)):
                row = '%s %s' % (i, self.list[i])
                f.write(row)

    def getList(self):
        return map(lambda x: x[:-1], self.list)
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

    # print(store.getNextOne())
    # myit = store.iterator()
    # for i in range(1000):
    #     print(store.getNextOne())


    # us = ['https://microsoft.com', 'http://courses.cse.tamu.edu/caverlee/csce670/']
    # store = URLs(us)
    # # print('test list')
    # for e in store.list:
    #     print(e)
    # print('test random url')
    # print(store.getRandomUrl())


if __name__ == '__main__':
    main()