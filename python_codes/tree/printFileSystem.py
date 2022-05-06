#!/usr/bin/python
import json
class Trie(object):
    def __init__(self):
        self.pCrawl = {}
        self.endOfFileSystem = '*'
    
    def insert(self, filePath):
        pCrawl = self.pCrawl
        for directory in filePath.split('/'):
            if directory not in pCrawl:
                pCrawl[directory] = {}
            pCrawl = pCrawl[directory]

    
    def printTrie (self):
        self.printTrieUtil(depth = 0, pCrawl = self.pCrawl)

    def printTrieUtil(self, depth = 0, pCrawl = {}):
        if pCrawl:
            for key in sorted(pCrawl.keys()):
                print ('#' + '  ' * depth  + '|----' + key)
                self.printTrieUtil(depth + 1 , pCrawl[key])

if __name__ == '__main__':
    paths = ['app/components/header', 'app/services', 'app/tests/components/header', 'images/image.png', 'index.html']
    t = Trie()
    for path in paths:
        t.insert(path)
    t.printTrie()    
        
