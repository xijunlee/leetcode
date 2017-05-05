#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f = [0 for i in xrange(len(nums))]
        if len(nums): f[0] = nums[0]
        else: return 0
        for i in range(1,len(nums)):
            cmp = -0x7fffffff
            if i - 2 >= 0:
                cmp = max(f[i-2]+nums[i],cmp)
            else:
                cmp = max(nums[i],cmp)
            cmp = max(f[i-1],cmp)
            f[i] = cmp
        return f[len(nums)-1]


if __name__ == '__main__':
    s = Solution()
    print s.rob([1,1])
