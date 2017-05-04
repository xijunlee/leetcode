#!/usr/bin/env python
# coding=utf-8

import sys
import pdb

if __name__ == "__main__":
    a = sys.stdin.readline().strip('\n')
    codes = sys.stdin.readline().strip('\n').split(':')
    ans = []
    #pdb.set_trace()
    if a == '0':
    	for v in codes:
    		i = 0
    		while i<len(v) and v[i] == '0': i += 1
    		ans.append(v[i:])
    	print ":".join(ans)
    else:
    	for v in codes:
    		ans.append('0'*(6-len(v))+v)
    	print ":".join(ans)

