#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        ret = []
        for i in xrange(len(input)):
            if input[i] == '+' or input[i] == '-' or input[i] == '*':
                part1Ret = self.diffWaysToCompute(input[:i])
                part2Ret = self.diffWaysToCompute(input[i+1:])
                for v1 in part1Ret:
                    for v2 in part2Ret:
                        c = 0
                        if input[i] == '+':
                            c = v1+v2
                        elif input[i] == '-':
                            c = v1-v2
                        elif input[i] == '*':
                            c = v1*v2
                        ret.append(c)
        if not len(ret):
            ret.append(int(input))
        return ret

if __name__ == '__main__':
    s = Solution()
    s.diffWaysToCompute("2-1-1")