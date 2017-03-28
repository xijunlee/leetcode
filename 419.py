#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    count += 1
                    k = i-1
                    while k>=0 and board[k][j] == 'X':
                        board[k][j] = '.'
                        k = k - 1
                    k = i+1
                    while k<len(board) and board[k][j] == 'X':
                        board[k][j] = '.'
                        k = k + 1
                    k = j-1
                    while k>=0 and board[i][k] == 'X':
                        board[i][k] = '.'
                        k = k - 1
                    k = j+1
                    while k<len(board[i]) and board[i][k] == 'X':
                        board[i][k] = '.'
                        k = k + 1
        
        return count
                    
                    