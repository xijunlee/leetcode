#!/usr/bin/env python
# coding=utf-8

import pdb

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        #pdb.set_trace()
        if int(num1)==0 or int(num2)==0:
            return '0'
        l1, l2 = len(num1), len(num2)
        ans = [0 for i in xrange(l1+l2)]
        num1r = num1[::-1]
        num2r = num2[::-1]
        for i in xrange(l1):
            for j in xrange(l2):
                ans[i+j] += int(num1r[i])*int(num2r[j])
        for i in xrange(1,len(ans)):
            ans[i] += ans[i-1]/10
            ans[i-1] %= 10
        ret = ''
        print ans
        for c in ans:
            ret+=str(c)
        if ans[l1+l2-1] == 0: ret = ret[:l1+l2-1]
        return ret[::-1]

if __name__ == '__main__':
    s = Solution()
    print s.multiply('999','999')



