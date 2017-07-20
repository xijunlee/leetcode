#!/usr/bin/env python
# coding=utf-8

import Queue

# bfs version
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        q = Queue.Queue()
        q.put([stones[0],0])
        source, target = stones[0], stones[-1]
        stones = set(stones)
        visited = set()
        visited.add(str(target)+'+0')
        while not q.empty():
            state = q.get()
            curPos, k = state[0], state[1]
            if curPos == target:
                return True

            if (curPos+k-1) in stones and str(curPos+k-1)+'+'+str(k-1) not in visited:
                q.put([curPos+k-1,k-1])
                visited.add(str(curPos+k-1)+'+'+str(k-1))

            if (curPos+k) in stones and str(curPos+k)+'+'+str(k) not in visited:
                q.put([curPos+k,k])
                visited.add(str(curPos+k)+'+'+str(k))

            if (curPos+k+1) in stones and str(curPos+k+1)+'+'+str(k+1) not in visited:
                q.put([curPos+k+1,k+1])
                visited.add(str(curPos+k+1)+'+'+str(k+1))
        return False

# dfs version 
class Solution(object):
    def canCross(self, stones):
        self.memo = set()
        target = stones[-1]
        stones = set(stones)

        res = self.bt(stones, 1, 1, target)
        return res

    def bt(self, stones, cur, speed, target):
        # check memo
        if (cur, speed) in self.memo:
            return False

        if cur==target:
            return True
        
        if cur>target or cur<0 or speed<=0 or cur not in stones:
            return False
        # dfs
        candidate = [speed-1, speed, speed+1]
        for c in candidate:
            if (cur + c) in stones:
                if self.bt(stones, cur+c, c, target):
                    return True

        self.memo.add((cur,speed))
        return False
if __name__ == '__main__':
    s = Solution()
    print s.canCross([0,2])



