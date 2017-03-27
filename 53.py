class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f = []
        for i in range(len(nums)):
            f.append(0)
        f[0] = nums[0]
        ret = -0x7fffffff
        for i in range(0,len(nums)):
            if i >= 1:
                f[i] = max(nums[i],f[i-1]+nums[i])
            ret = max(ret,f[i])
        return ret
                