#!/usr/bin/env python
# coding=utf-8

'''
so easy!!!
'''

class Solution(object):
    count = 0
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        board = [['.' for i in range(n)] for j in range(n)]
        
        def dfs(step, b):
        	if step >= n:
        		self.count += 1
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
        
        return self.count