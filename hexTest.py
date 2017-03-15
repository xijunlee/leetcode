#!/usr/bin/env python
# coding=utf-8

count = 0 
for i in range(7):
    count+=15 * (16 ** i)
count += 7*(16**7)
print count
