#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        flag = False
        if word.upper() == word:
            flag = True
        
        if word.lower() == word:
            flag = True
       
        if word.capitalize() == word:
            flag = True
        
        
        return flag

