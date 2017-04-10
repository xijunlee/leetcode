#!/usr/bin/env python
# coding=utf-8

'''学到了：
1、Python的字符串和list的分片技术，s[i:j:step],从i出发，一直到j不包括j，步长为step。
2、要巧妙地利用str->list后，list有reverse()这个函数，但是翻转后不能直接str(l)，得用''.join()
   操作来链接list中的每个元素

'''

# method 1

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

# method 2

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1 = list(s)
        s1.reverse()
        return ''.join(s1)


