#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        h = len(triangle)
        f = []
        for i in range(h):
            f.append([0 for j in range(len(triangle[i]))])
        f[0][0] = triangle[0][0]
        for i in range(1,h):
            f[i][0] = f[i-1][0] + triangle[i][0]
            f[i][-1] = f[i-1][-1] + triangle[i][-1]
            for k in range(1,len(triangle[i])-1):
                f[i][k] = min(f[i-1][k-1],f[i-1][k])+triangle[i][k]
        return min(f[h-1])

if __name__ == '__main__':
	s = Solution()
	print s.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])
        