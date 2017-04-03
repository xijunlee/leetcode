#!/usr/bin/env python
# coding=utf-8

class Solution(object):
	
	count = 0
	l = 0
	def countArrangement(self, N):
		"""
		:type N: int
		:rtype: int
		"""
		visited = [0 for i in range(N+1)]
		self.l = N
		self.dfs(1,visited)
		return self.count 

	def dfs(self, step, visited):
		if step > self.l:
			self.count += 1
			return

		for i in range(1, self.l+1):
			if not visited[i] and (i%step==0 or step%i==0):
				visited[i] = 1
				self.dfs(step+1, visited)
				visited[i] = 0
		return

if __name__ == '__main__':
	s = Solution()
	print s.countArrangement(4)

