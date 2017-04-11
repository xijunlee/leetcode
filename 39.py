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

if __name__ == '__main__':
    s = Solution()
    print s.combinationSum([2, 3, 6, 7], 7)