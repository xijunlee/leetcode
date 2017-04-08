#!/usr/bin/env python
# coding=utf-8

'''
学到了：
1、python表达式是直接算出来布尔值的！！可以直接跟在return后面
2、dict添加元素的方法就是直接dict[key]=value，很暴力
3、复习了动态规划的递归解法，以及其memorization，递归的话就会要用到memo来保存已经计算过的值，能有效去除重复计算\\
    而如果采用循环的方法来做动态规划的话，由于是从底层开始往上计算的，那么上层要用的计算结果就肯定已经\\
    计算出现过了，所以就不会出现重复的计算。而递归的话，由于是从上往下的，那么上层的计算可能会重复用到\\
    下层的结果。如果不采用数组保存已经计算过的结果，那么上层会重复调用下层计算，带来不必要的时间开销。
'''

class Solution(object):
    memo = {}
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.helper(nums,0,len(nums)-1) >= 0

    def helper(self, nums, st, ed):
        if (st,ed) not in self.memo.keys():
            if st == ed: self.memo[(st,ed)] = nums[st]
            else: self.memo[(st,ed)] = max(nums[st] - self.helper(nums,st+1,ed), nums[ed] - self.helper(nums,st,ed-1))
        return self.memo[(st,ed)]

if __name__ == '__main__':
    s=Solution()
    print s.PredictTheWinner([1,1,1])
