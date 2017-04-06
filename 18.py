#!/usr/bin/env python
# coding=utf-8

'''
很巧妙的思路：
    0、先对nums进行排序
    1、把n sum的问题递归分治成n-1 sum, n-2 sum, ...的问题，最后划分到2 sum的最小子问题，然后利用二分查找来求解2 sum的问题（求解两个数等于target)
    2、巧妙地在递归中传递中间结果，然后将合法结果添加到最终的结果list中去

学到了：
    1、Python中list 是可以直接相加的，比如[a]+[b] = [a,b]
    2、python中list的append是在堆上执行的

'''

class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results

    def findNsum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2: return

        # solve 2-sum
        if N == 2:
            l,r = 0,len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]: # remove duplicate
                        l += 1
                    while r > l and nums[r] == nums[r + 1]: # remove duplicate
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums)-N+1):   # careful about range
                if target < nums[i]*N or target > nums[-1]*N:  # take advantages of sorted list
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:  # recursively reduce N
                    self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
        return
        