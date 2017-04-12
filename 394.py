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
                tmp, num = '', ''
                while len(stack) and stack[-1] != '[':
                    tmp += stack.pop()
                stack.pop()
                while len(stack) and ord(stack[-1])>=48 and ord(stack[-1])<=57:
                    num += stack.pop()
                num = int(num[::-1])
                for v in num*tmp[::-1]: # flat the repeated string into the stack
                    stack.append(v)
            p += 1
        for c in stack:
            retStr += c
        return retStr
