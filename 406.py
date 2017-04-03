#!/usr/bin/env python
# coding=utf-8

import pdb
'''
Pick out tallest group of people and sort them in a subarray (S). Since there's no other groups of people taller than them, therefore each guy's index will be just as same as his k value.
For 2nd tallest group (and the rest), insert each one of them into (S) by k value. So on and so forth.
E.g.
input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
subarray after step 1: [[7,0], [7,1]]
subarray after step 2: [[7,0], [6,1], [7,1]]
'''

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        ret , sub, i= [], [], 0
        people.sort(key = lambda x: x[0],reverse = True)
        while i < len(people):

        	sub = []
        	for j in range(i,len(people)):
        		if people[j][0] < people[i][0]:
        			break
        		sub.append(people[j])
        	i += len(sub)
        	sub.sort(key = lambda x:x[1])
        	for v in sub:
        		ret.insert(v[1],v)

        return ret





if __name__ == '__main__':
	s = Solution()
	print s.reconstructQueue([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]])

