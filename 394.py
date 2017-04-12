#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        p, retStr = 0, ''
        stack = []
        flag = 0
        while p < len(s):
            if s[p] != ']': stack.append(s[p]) # push element into stack
            else:
                tmp1, tmp2, num = retStr, '', ''
                while len(stack) and stack[-1] != '[':
                    tmp = stack.pop()
                    tmp1 += tmp
                    tmp2 += tmp
                stack.pop()
                while len(stack) and ord(stack[-1])>=48 and ord(stack[-1])<=57:
                    num += stack.pop()
                num = int(num[::-1])
                if flag == 0:
                    retStr += num*tmp2[::-1]
                    if (len(stack) and ord(stack[-1]) >= 97 and ord(stack[-1])<=122):
                        flag = 1
                else:
                    retStr = num*tmp1[::-1]
                    if not (len(stack) and ord(stack[-1]) >= 97 and ord(stack[-1])<=122):
                        flag = 0
            p += 1
        for c in stack:
            retStr += c
        return retStr

if __name__ == '__main__':
	s = Solution()
	print s.decodeString("100[leetcode]")
