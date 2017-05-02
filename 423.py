#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        alphabeta = 'abcdefghijklmnopqrstuvwxyz'
        num = ['zero','one','two','three','four','five','six','seven','eight','nine']
        d = {}
        for v in alphabeta:
            d[v]=s.count(v)
        ans = {}
        ans['0'] = d['z']
        for c in num[0]:
            d[c]-=ans['0']
        ans['2'] = d['w']
        for c in num[2]:
            d[c]-=ans['2']
        ans['4'] = d['u']
        for c in num[4]:
            d[c]-=ans['4']
        ans['6'] = d['x']
        for c in num[6]:
            d[c]-=ans['6']
        ans['8'] = d['g']
        for c in num[8]:
            d[c]-=ans['8']

        ans['1'] = d['o']
        for c in num[1]:
            d[c]-=ans['1']
        ans['3'] = d['t']
        for c in num[3]:
            d[c]-=ans['3']
        ans['5'] = d['f']
        for c in num[5]:
            d[c]-=ans['5']
        ans['7'] = d['v']
        for c in num[4]:
            d[c]-=ans['7']

        ans['9'] = d['i']
        for c in num[9]:
            d[c]-=ans['9']

        ansStr = ''
        for n in xrange(10):
            k = str(n)
            v = ans.get(k)
            ansStr+=v*k
        return ansStr

if __name__ == '__main__':
    s = Solution()
    s.originalDigits("fviefuro")


