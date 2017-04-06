#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    hash = []

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        self.hash = [0 for i in range(N)]
        h_count = 1
        for i in range(N):
            if not self.hash[i]:
                for j in range(N):
                    if M[i][j] and self.hash[j]:
                        self.hash[i] = self.hash[j]
                        break
                else:
                    self.hash[i] = h_count
                    h_count += 1
            dset = []
            for j in range(N):
                if i!=j and M[i][j] and self.hash[i] != self.hash[j]: dset.append(j)
            self.union_set(M,self.hash[i],dset)

        return len(set(self.hash))

    def union_set(self, M, h_value, dset):
        if dset:
            for i in dset:
                tmp = []
                self.hash[i] = h_value
                for j in range(len(M)):
                    if i!=j and M[i][j] and self.hash[i] != self.hash[j]: tmp.append(j)
                self.union_set(M,self.hash[i],tmp)
        return
if __name__ == '__main__':
     
     s = Solution()
     print s.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])
            