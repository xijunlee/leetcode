#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        x, y, visited, ret = [1,0,-1,0], [0,1,0,-1], [], []
        m, n, c = len(matrix), len(matrix[0]), 0
        i, j, k = 0, 0, 0
        while c < m*n:
            if (str(i)+str(j)) not in visited:
                ret.append(matrix[i][j])
                visited.append(str(i)+str(j))
                c += 1
            ii, jj = i+y[k], j+x[k]
            if ii>=0 and ii< m and jj>=0 and jj<n and (str(ii)+str(jj)) not in visited:
                i, j = ii, jj
            else:
                k = (k+1)%4
        return ret

