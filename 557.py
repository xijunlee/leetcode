#!/usr/bin/env python
# coding=utf-8
'''
学到了：
字符串可以通过分片做到倒序输出：word[::-1]
'''


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')
        words2 = []
        for word in words:
            words2.append(word[::-1])
        return ' '.join(words2)

