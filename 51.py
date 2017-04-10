#!/usr/bin/env python
# coding=utf-8

'''
so easy!!!
'''

import copy

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        tmp, ret = [], []
        board = [['.' for i in range(n)] for j in range(n)]
        def dfs(step, b):
        	if step >= n:
        		tmp.append(copy.deepcopy(b))
        		return
        	for j in range(n):
        		if b[step][j] == '.':
        			flag = True
        			for i in range(n):
        				if step != i and b[i][j] == 'Q':
        					flag = False
        					break

        			ii, jj = step-1, j-1
        			while ii>=0 and ii<n and jj>=0 and jj<n:
        				if b[ii][jj] == 'Q':
        					flag = False
        					break
        				ii -= 1
        				jj -= 1

        			ii, jj = step-1, j+1
        			while ii>=0 and ii<n and jj>=0 and jj<n:
        				if b[ii][jj] == 'Q':
        					flag = False
        					break
        				ii -= 1
        				jj += 1

        			ii, jj = step+1, j+1
        			while ii>=0 and ii<n and jj>=0 and jj<n:
        				if b[ii][jj] == 'Q':
        					flag = False
        					break
        				ii += 1
        				jj += 1

        			ii, jj = step+1, j-1
        			while ii>=0 and ii<n and jj>=0 and jj<n:
        				if b[ii][jj] == 'Q':
        					flag = False
        					break
        				ii += 1
        				jj -= 1
        			if flag:
        				b[step][j] = 'Q'
        				dfs(step+1,b)
        				b[step][j] = '.'
        dfs(0,board)
        for s in tmp:
            s1 = []
            for row in s:
                s1.append("".join(row))
            ret.append(s1)
        return ret

if __name__ == '__main__':
	s = Solution()
	print s.solveNQueens(4)

