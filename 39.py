#!/usr/bin/env python
# coding=utf-8

import copy

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []

        def dfs(sum, step, stack):

            if step>=len(candidates) or sum>target:
                return
            if sum == target:
                flag = True
                for s in ret:
                    if s == stack:
                        flag = False
                        break
                if flag == True: ret.append(copy.deepcopy(stack))
                return
            if sum + candidates[step] < target:
                stack.append(candidates[step])
                dfs(sum+candidates[step],step,stack)
                dfs(sum+candidates[step],step+1,stack)
                stack.pop()
                dfs(sum,step+1,stack)
            return

        candidates.sort()
        dfs(0,0,[])
        return ret

class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
    
    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return 
        for i in xrange(index, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)

if __name__ == '__main__':
    s = Solution()
    print s.combinationSum([2, 3, 6, 7], 7)