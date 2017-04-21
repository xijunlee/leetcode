#!/usr/bin/env python
# coding=utf-8

'''
python字符串的分片可以写超过字符串长度的下标，但是超过字符串长度下标的分片是会返回空字符串的。
'''

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s1 = ''.join(S.upper().split('-'))
        s2 = s1[::-1]
        ret = ''
        for i in range(0,len(s2),K):
            ret += s2[i:i+K] 
            if i+K < len(s2): ret += '-'
        return ret[::-1]

if __name__ == '__main__':
	s = Solution()
	print s.licenseKeyFormatting("2-4A0r7-4k",3)