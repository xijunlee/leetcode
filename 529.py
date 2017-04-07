#!/usr/bin/env python
# coding=utf-8

'''
这个题目很无聊，纯粹考操作和递归，居然没看清楚矩阵可以不是方的，还检查了好一会儿
'''

class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if board[click[0]][click[1]] == 'M': self.revealMine(board,click)
        if board[click[0]][click[1]] == 'E': self.revealEmptySquare(board,click)

        return board

    def revealMine(self, board, click):

		board[click[0]][click[1]] = 'X'
		return

    def revealEmptySquare(self, board, click):
    	xl = len(board)
    	yl = len(board[0])
    	adjList = []
    	count = 0
    	idir = [-1,-1,-1,0,1,1,1,0]
    	jdir = [-1,0,1,1,1,0,-1,-1]
    	for i in range(8):
            x, y = click[0]+idir[i], click[1]+jdir[i]
            if x>=0 and x<xl and y>=0 and y<yl:
    		  if board[x][y] == 'M':
    		    count += 1
    		  elif board[x][y] == 'E':
    			adjList.append([x,y])
    	if count:
    		board[click[0]][click[1]] = str(count)
    	else:
    		board[click[0]][click[1]] = 'B'
    		for c in adjList:
    			self.revealEmptySquare(board, c)
    	return 

if __name__ == '__main__':
	
	s = Solution()
	print s.updateBoard([['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']],[3,0])