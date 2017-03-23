#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        longS = ''
        shortS = ''
        
        if len(s) != len(t):
            return False
        longS = s
        shortS = t
        ld={}
        sd={}
        for item in set(longS):
            ld[item] = longS.count(item)
        for item in set(shortS):
            sd[item] = shortS.count(item)
        flag = True
        for item in ld.keys():
            if sd.has_key(item):
                if ld[item] != sd[item]:
                    flag = False
                    break
            else:
                flag = False
                break
        return flag
        
        