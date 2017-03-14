#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ret = []
        f = set('qwertyuiop')
        s = set('asdfghjkl')
        t = set('zxcvbnm')
        keyRows = [f,s,t]
        
        for str in words:
            lstr = set(str.lower())
            flag = False
            for row in keyRows:
                if lstr.issubset(row):
                    flag = True
                    break
            if flag == True:
                ret.append(str)
                
        return ret      
            