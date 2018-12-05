
from __future__ import print_function
import sys
import random
import os
from graph import *
from record import *

class URLs:
    # save the list , have two btn, continue, or new url

    def __init__(self, update_url = False):
        '''
         diff cases:
         1, need to update url
         2, have a set file and list file
         '''

        self.data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'urlDictionary.data')
        self.crawl_result = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'clx/clx/crawl_result.csv')
        self.set_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'url_set.pickle')
        self.id = 0
        if not os.path.isfile(self.data_file) or os.path.getsize(self.data_file) == 0:
            update_url = True
        
        if update_url:
            print('loading new urls...')
            self.update_urls_datafile(self.data_file)
            
            self.save_set()
        else:
            if os.path.isfile(self.set_file):
                self.load_set()
                print(f'{self.set_file} does exist.')
                print(self.set)
            else:
                print(f'{self.set_file} does not exist. please update url first.')
                urls = []
                with open(self.data_file, 'r+') as f:
                    for line in f.readlines():
                        tmp = line.split(' ')
                        urls.append(tmp[len(tmp) - 1][:-1])
                self.list = urls
                self.create_set()
                self.save_set()

        #set([str(i) for i in range(app.k)])
        # self.app.k = len(self.list)

    def load_set(self):
        self.set = load_pickle(self.set_file)
         
        urls = []
        with open(self.data_file, 'r') as f:
            for line in f.readlines():
                tmp = line.split(' ')
                urls.append(tmp[len(tmp) - 1][:-1])
        self.list = urls
        
    def create_set(self):
        self.set = set([str(x) for x in range(len(self.list))])
    
    def save_set(self):
        save_pickle(self.set_file, self.set)

    def crawl_result_2_urllists(self):
        import csv
        urls = []
        if not os.path.isfile(self.crawl_result):
            print(f'currenly no {self.crawl_result} exists')
            self.list = urls
            return 
        with open(self.crawl_result) as f:
            csv_reader = csv.reader(f, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print ('Column names are %s' % (", ".join(row)) )
                    line_count += 1
                else:
                    if row is None or len(row) == 0:
                        continue
                    print( row[0])
                    urls.append(row[0])
                    # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                    line_count += 1
            print('Processed %d lines.'% line_count)
        self.list = urls

    def update_urls_datafile(self, fname):
        self.crawl_result_2_urllists()
        with open(fname, 'w+') as f:
            for i in range(len(self.list)):
                row = '%s %s\n' % (i, self.list[i])
                f.write(row)
        self.create_set() 
        # self.set = set([x for x in range(len(self.list))])

    def get_all_used_urls(self):
        used_urls = []
        for url in self.list:
            if url not in self.set:
                used_urls.append(url)
        return used_urls

    def getList(self):
        return map(lambda x: x, self.list)
        # return self.list

    def iterator(self):
        # @deprecate
        self.id = 0
    #     self.it = iter(self.set)
    #     return self.it

    def getNext(self):
        if len(self.set) == 0:
            return "reach the end"
        rm_id = self.get_random_url_id()
        return self.get_next_by_id(rm_id)

    def remove_from_id(self, rm_id):
        # @disabled
        # self.set.remove(rm_id)
        print(self.set)

    def get_next_by_id(self, rm_id):
        print(self.set)
        rm_id = int(rm_id)
        self.id = rm_id
        return self.list[rm_id]

    def get_random_url_id(self):
        self.random_list = list(self.set)
        idx = random.randint(0, len(self.random_list) - 1)
        rm_id = self.random_list[idx]
        return rm_id # str id


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