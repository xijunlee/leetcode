#!/usr/bin/env python
# coding=utf-8

import sys

if __name__ == "__main__":
    T = sys.stdin.readline().strip('\n')
    ans = []
    for i in xrange(T):
        line = sys.stdin.readline().strip('\n')
        if line[0] == 'R' and ord(line[1])>=0 and ord(line[1])<=9:
        	i = 1
        	while i < len(line) and line[i]!='C':
        		i+=1
        	r_num = line[1:i]
        	c_num = int(line[i:len(line)-1])
        	rc = []
        	while c_num > 0:
        		rc.append(chr(c_num%26-1+ord('A')))
        		c_num /= 26
        	ans.append(rc[::-1]+r_num)
    for v in ans:
    	print v


