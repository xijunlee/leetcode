#!/usr/bin/env python
# coding=utf-8

import Queue
import pdb

class Node(object):
    def __init__(self, w, l, le):
        self.word = w
        self.level = l
        self.left = le

class Solution(object):

    def wordEqualOne(self,w1,w2):
        if w1 == w2:
            return False
        for i in xrange(len(w1)):
            newW1 = w1[0:i]+w1[i+1:]
            newW2 = w2[0:i]+w2[i+1:]
            if newW1 == newW2:
                return True
        return False

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        Q = Queue.Queue()
        Q.put(Node(beginWord,1,[i for i in xrange(len(wordList))]))
        #pdb.set_trace()
        while not Q.empty():
            current = Q.get()
            print current.word,current.level 
            if current.word == endWord:
                return current.level
            tmp, characterList = [], 'qwertyuiopasdfghjklzxcvbnm'
            for i in xrange(len(current.word)):
                for c in characterList:
                    tmp.append(current.word[0:i]+c+current.word[i+1:])
            tmp = set(tmp)
            for item in current.left:
                left_to_next = current.left[:]
                #print left_to_next
                #print wordList[item]
                #print len(set(current.word)-set(wordList[item]))
                if wordList[item] in tmp:
                    left_to_next.remove(item)
                    
                    newNode = Node(wordList[item],current.level+1,left_to_next)
                    Q.put(newNode)
        return 0

if __name__ == '__main__':
    s = Solution()
    print s.ladderLength("leet",
"code",
["lest","leet","lose","code","lode","robe","lost"])

