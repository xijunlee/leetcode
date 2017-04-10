#!/usr/bin/env python
# coding=utf-8

from heapq import *

if __name__ == '__main__':
	a = [1,3,5,9,2]
	'''
	h = []
	for v in a:
		heappush(h,v)
	print [heappop(h) for i in range(len(h))]
	'''
	heapify(a)
	print [heappop(a) for i in range(len(a))]
