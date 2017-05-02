#!/usr/bin/env python
# coding=utf-8

import sys
import pdb

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip('\n'))
    ans = []
    for i in xrange(T):
        line = sys.stdin.readline().strip('\n')
        if line[0] == 'R' and ord(line[1])>=48 and ord(line[1])<=57:
        	i = 1
        	while i < len(line) and line[i]!='C':
        		i+=1
        	r_num = line[1:i]
        	c_num = int(line[i+1:])
        	rc = ''
        	#pdb.set_trace()
        	while c_num > 0:
        		tmp = c_num%26
        		rc+=chr(tmp-1+ord('A'))
        		c_num /= 26
        	ans.append(rc[::-1]+r_num)
        else:
        	i = 0
        	pdb.set_trace()
        	while i<len(line) and line[:i+1].isalpha():
        		i += 1
        	r_num = int(line[i:])
        	c = line[0:i]
        	k, c_num = 1, 0
        	for i in xrange(len(c)-1,-1,-1):
        		c_num += (ord(c[i])-ord('A')+1)*k
        		k*=26
        	ans.append('R'+str(r_num)+'C'+str(c_num))
    for v in ans:
    	print v


