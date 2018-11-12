import os
import numpy as np
from record import *

class graph:
    def __init__(self, app, new = False):
        self.app = app
        self.childOf = {}
        self.nodes = app.k
        
        self.parents_file = f'{os.path.dirname(os.path.abspath(__file__))}/parents.pickle'
        print(f'{self.parents_file} does exist.')
        # UNION FIND
        if new:
            self.parents = [(x) for x in range((app.k))]
            self.save()
        else:
            if os.path.isfile(self.parents_file):
                self.parents = load_pickle(self.parents_file)
            else:
                self.parents = [(x) for x in range((app.k))]

        self.score = np.zeros(self.nodes)
        self.score = self.score - np.ones(self.nodes)
    
    def save(self):
        save_pickle(self.parents_file, self.parents)

    def add_edge(self, a, b, idx):
        if idx == 0:
            # a b, a > b
            self.childOf[a] = b
            self.union(int(a), int(b))
        else:
            # b > a, b a
            self.childOf[b] = a
            self.union(int(b), int(a))
        # self.getScores()

    def union(self, a, b):
        a = int(a)
        b = int(b)
        root1 = self.find(a)
        root2 = self.find(b)
        if root1 == root2:
            pass
            # in the same tree
        else:
            # assumption: if a > b, root1 > root2
            self.parents[root2] = root1
        return True

    def find(self, ids):
        ids = int(ids)
        while ids != self.parents[ids]:
            ids = self.parents[ids]
        return ids
# TODO
    def get_topological_sort(self):
        nexts = {} # from the least one to the bigger related ones,
        outs = np.zeros(self.nodes)
        for p in self.childOf:
            outs[p]+= 1
            if self.childOf[p] not in nexts:
                nexts[self.childOf[p]] = []
            nexts[self.childOf[p]].append(p)
        source = -1
        for p in range(len(outs)):
            if outs[p] == 0:
                source = p



    def getScores(self):
        
        '''
        4
        3, 2
        0
        1
        4-3, 3-0, 0-1, 2-0
        to
        1-0
        0-3,2
        3-4
        '''
        print(self.parents)


        self.score = np.zeros(self.nodes)
        self.score = self.score - np.ones(self.nodes)
        # record indegree of allself.nodes, if in degreee == 0, is a leaf
        nexts = {} # from the least one to the bigger related ones,
        outs = np.zeros(self.nodes)
        for p in self.childOf:
            outs[p]+= 1
            if self.childOf[p] not in nexts:
                nexts[self.childOf[p]] = []
            nexts[self.childOf[p]].append(p)
        source = -1
        for p in range(len(outs)):
            if outs[p] == 0:
                source = p

        # bfs from the source 
        q = []
        q.append(source)
        sc = 0
        while len(q) != 0:
            size = len(q)
            for i in range(size):
                cur = q.pop(0)
                self.score [cur] = sc
                if cur not in nexts:
                    continue
                q.extend(nexts[cur])
            sc += 1
            
        sc -= 1
        # sc is the max score
        # for i in range(len(score)):
        #     score[i] = float(score[i] / sc)
        return self.score

    def find_with_path(self, ids):
        ids = int(ids)
        path = 0
        while ids != self.parents[ids]:
            ids = self.parents[ids]
            path += 1
        return ids, path
    
    def exist_edge(self, a, b):
        a = int(a)
        b = int(b)
        root1 = self.find(a)
        root2 = self.find(b)
        if root1 == root2:
            return True
            # in the same tree
        else:
            return False
    
    def compare(self, a, b):
        a = int(a)
        b = int(b)
        root1, p1 = self.find_with_path(a)
        root2, p2 = self.find_with_path(b)
        if root1 == root2:
            return p1 - p2
            # in the same tree
        else:
            raise ValueError(f'{a} and {b} not in the same tree')