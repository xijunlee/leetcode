#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d1, d2 = {}, {}
        for c in ransomNote:
            if not d1.has_key(c): d1[c]=1
            else: d1[c]+=1
        for c in magazine:
            if not d2.has_key(c): d2[c]=1
            else: d2[c]+=1
        flag = True
        for k in d1.keys():
            if k not in d2 or d2[k]<d1[k]:
                flag = False
                break
        return flag

