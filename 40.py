#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        def dfs(index, target, path):
            if target == 0 and path not in ret:
                ret.append(path)
                return
            if target < 0 or index >= len(candidates):
                return
            if target - candidates[index] >= 0:
                dfs(index+1,target-candidates[index],path+[candidates[index]])
                dfs(index+1,target,path)
            return
        
        candidates.sort()
        dfs(0,target,[])

        return ret
if __name__ == '__main__':
	s = Solution()
	print s.combinationSum2([1],1)
