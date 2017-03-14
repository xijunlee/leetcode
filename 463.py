#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ret = 0
        xl = len(grid)
        for x in range(xl):
            yl = len(grid[x])
            for y in range(yl):
                if grid[x][y] == 1:
                    count = 0
                    if x-1 >= 0:
                        if grid[x-1][y] == 1:
                            count += 1
                    if x+1 <= xl-1:
                        if grid[x+1][y] == 1:
                            count += 1
                    if y+1 <= yl-1:
                        if grid[x][y+1] == 1:
                            count += 1
                    if y-1 >= 0:
                        if grid[x][y-1] == 1:
                            count += 1
                    count = 4 - count
                    ret += count
        return ret
        

