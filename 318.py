#!/usr/bin/env python
# coding=utf-8

'''
其实思路很简单，如果直接对两个单词的set进行&运算，速度会慢很多。但是如果变成对位进行&运算就会快很多
1、将每个词转换成相应的32位bit
2、O(n2)时间内，任取两个词计算其32位bit的&，如果存在common letter,则&结果不为零。取&为零的两个词，计算单词长度乘积，保留最大乘积作为结果返回。
'''

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        word2=[]
        for word in words:
            tmp = 0
            for c in set(word):
                tmp += 1 << (ord(c)-97)
            word2.append(tmp)
        ret = 0
        for i in range(len(word2)):
        	for j in range(i+1,len(word2)):
        		if not word2[i] & word2[j]:
        			ret = max(ret,len(words[i])*len(words[j]))
        return ret
if __name__ == '__main__':
	 s = Solution()
	 print s.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])