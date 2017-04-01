#!/usr/bin/env python
# coding=utf-8
import pdb

class Solution(object):

	def __init__(self,N,P,Q):
		self.N = N
		self.P = P
		self.Q = Q
		self.longest = 0

	def searchLongest(self):

		step = 0
		l = 0
		p = self.P
		while l < self.N:
			if p < 100:
				p += self.Q
			elif p>= 100:
				l += 1
				p = self.P/2**l
			step += 1
		return step

	def solve(self):
		ret = 0
		maxStep = self.searchLongest()
		for k in range(0,2**maxStep):
			tmp = k
			path = []
			while tmp>0: 
				path.append(tmp & 1)
				tmp = tmp >> 1

			if sum(path) == self.N:
				flag = True
				i = 0
				p = self.P
				ans = len(path)
				while flag and i<len(path):
					if path[i]==0 and p< 100:
						ans *= (100-p)
						p = p + self.Q
					elif path[i] == 0 and p>= 100:
						flag = False
						break
					if path[i]==1:
						if p>= 100: ans *= 100
						else: ans*=p
						p = self.P/2**sum(path[:i+1])
					i += 1
				ans /= (100.0)**(len(path))
				ret += ans
		return ret


if __name__ == '__main__':
	(P,Q,N) = (int(x) for x in raw_input().split())
	s = Solution(N,P,Q)
	print "%.2f" % s.solve()


