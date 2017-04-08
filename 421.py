#!/usr/bin/env python
# coding=utf-8
'''
这道题学到了好多啊：
1、Trie树的知识，以及如何快速地利用python的dict建立Trie树，实在是太方便了
2、位运算的再一次复习，发现还是不熟位运算！！！

解题思路：
1、按nums中每个数建立一个Trie树，一定要按照高位到低位来建树，因为在高位的1更“值钱”
2、根据nums中每一个数，去找与它最不相同的数，即亦或值最大
'''


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # building Trie tree
        root = dict()
        _end = '_end'
        for num in nums:
            current_dict = root
            for i in range(31,-1,-1): 
                current_dict = current_dict.setdefault((num>>i)&1, {})
            current_dict[_end] = num
        # calculating maximum Xor
        ret = 0
        for num in nums:
            xor = 0
            current_dict = root
            for i in range(31,-1,-1):
                bit = 1 << i
                if num & bit > 0:
                    if current_dict.get(0):
                        current_dict = current_dict[0]
                        xor += bit
                    else: current_dict = current_dict[1]
                else:
                    if current_dict.get(1):
                        current_dict = current_dict[1]
                        xor += bit
                    else: current_dict = current_dict[0]
            ret = max(ret,xor)
        return ret

if __name__ == '__main__':
    s = Solution()
    print s.findMaximumXOR([3, 10, 5, 25, 2, 8])
