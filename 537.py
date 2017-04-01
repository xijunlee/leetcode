#!/usr/bin/env python
# coding=utf-8
import pdb

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #pdb.set_trace()
        arr1 = a.split('+')
        arr2 = b.split('+')
        r1, r2 = int(arr1[0]), int(arr2[0])
        v1, v2 = int(arr1[1].strip('i')), int(arr2[1].strip('i'))
        r = r1*r2 - v1*v2
        v = r1*v2 + v1*r2
        r = str(r)
        v = str(v)+'i'
        return r+'+'+v

if __name__ == '__main__':
	s = Solution()
	print s.complexNumberMultiply("1+1i","1+1i")



