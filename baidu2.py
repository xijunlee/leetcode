#!/usr/bin/env python
# coding=utf-8

import sys

def ave(a):
	if len(a) == 0: return 0
	else: return float(sum(a))/len(a)
def min1(a):
	if len(a) == 0: return 0
	else: return min(a)

def max1(a):
	if len(a) == 0: return 0
	else: return max(a)

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip('\n'))
    time, val = [], []
    for i in xrange(N):
    	t, v = sys.stdin.readline().strip('\n').split(' ')
    	time.append(int(t))
    	val.append(int(v))
    C = int(sys.stdin.readline().strip('\n'))
    for c in xrange(C):
    	R, F, L = sys.stdin.readline().strip('\n').split(' ')
    	count = 0
    	for i in xrange(N):
    		j = i-1
    		while j>=0 and (time[j]<time[i] and time[j]>=time[i]-int(L)):
    			j -= 1
    		tmp = val[j+1:i]
    		if R == 'gt':
    			if F == 'min': 
    				if len(tmp) and val[i]>min(tmp): count+=1
    			elif F == 'max':
    				if len(tmp) and val[i]>max(tmp): count+=1
    			elif F == 'avg':
    				if len(tmp) and  val[i]>ave(tmp): count+=1
    		elif R == 'lt':
    			if F == 'min': 
    				if len(tmp) and val[i]<min(tmp): count+=1
    			elif F == 'max':
    				if len(tmp) and val[i]<max(tmp): count+=1
    			elif F == 'avg':
    				if len(tmp) and val[i]<ave(tmp): count+=1
    	print count




