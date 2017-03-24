#!/usr/bin/env python
# coding=utf-8

import pdb

class Solution(object):
    def readBinaryWatch(self, num):
        ret = []
        if num == 0:
            ret.append('0:00')

        for i in range(1024):
            l = []
            k = i
            while k > 0:
                l.append(k%2)
                k /= 2
            if l.count == num:
                pdb.set_trace()
                high = i & (15 << 8)
                low = i & 255
                if low < 10:
                    ret.append(str(high)+':0'+str(low))
                else:
                    ret.append(str(high)+':'+str(low))
        return ret


if __name__ == '__main__':

	s = Solution()
	print type(s)
	pdb.set_trace()
	s.readBinaryWatch(1)

