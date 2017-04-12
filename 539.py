#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        ret = 0xfffffff
        '''
        for i in range(len(timePoints)):
        	h1, m1 = int(timePoints[i][0:2]), int(timePoints[i][3:5])
        	t1 = h1*60 + m1
        	for j in range(i+1,len(timePoints)):
        		h2, m2 = int(timePoints[j][0:2]), int(timePoints[j][3:5])
        		t2 = h2*60 + m2
        		ret = min(ret,min([abs(t1-t2),abs(24*60+t1-t2),abs(t1-t2-24*60)]))
        '''
        times = []
        for v in timePoints:
            h, m = int(v[0:2]), int(v[3:5])
            t = h*60 + m1
            times.append(t)
            if t < 12*60: times.append(t+24*60)
        times.sort()
        for i in range(1,len(times)):
            ret = min(ret,abs(times[i]-times[i-1]))

        return ret

if __name__ == '__main__':
	s = Solution()
	print s.findMinDifference(["23:59","00:00"])