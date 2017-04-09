#!/usr/bin/env python
# coding=utf-8

import pdb

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count = 0
        d = {}

        for p in points:
            for q in points:
                if p!=q:
                    dis = (p[0]-q[0])**2 + (p[1]-q[1])**2
                    if not d.has_key(dis):
                        d[dis] = 1
                    else:
                        d[dis] += 1
        for val in d.values():
            count += (val/2)*(val/2-1)
        return count

if __name__ == '__main__':
	s = Solution()
	print s.numberOfBoomerangs([[0,0],[1,0],[2,0]])
