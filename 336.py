#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        worddict = {}
        ret = []
        for i in xrange(len(words)):
            worddict[words[i]] = i

        for i in xrange(len(words)):
            for j in xrange(len(words[i])):
                s1 = words[i][:j]
                s2 = words[i][j:]
                #print s1+', ' + s2
                if s1[::-1] in worddict and worddict[s1[::-1]] != i and s2 == s2[::-1]:
                    ret.append([i,worddict[s1[::-1]]])
                if s2[::-1] in worddict and worddict[s2[::-1]] != i and s1 == s1[::-1]:
                    ret.append([worddict[s2[::-1]],i])
                if j == 0 and s1 in worddict and worddict[s1] != i and s2 == s2[::-1]:
                    ret.append([worddict[s1],i])
        return ret

if __name__ == '__main__':
    s = Solution()
    print s.palindromePairs(["a",""])
                    

