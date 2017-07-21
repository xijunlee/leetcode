#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    
    def __init__(self,str1,str2):
        self.s1, self.s2 = str1, str2

    def concatenateString(self):
        self.conStr = self.s1+self.s2
        print 'The result of conatenating two strings is: ',self.conStr

    def sortString(self):
        oddList, evenList = [], []
        for i in xrange(len(self.conStr)):
            if i % 2 == 0: evenList.append(self.conStr[i])
            else: oddList.append(self.conStr[i])
        self.qsort(oddList,0,len(oddList)-1)
        self.qsort(evenList,0,len(evenList)-1)

        tmp = ''
        for i in xrange(len(self.conStr)):
            if i%2 == 0: tmp+=evenList[i/2]
            else: tmp+=oddList[(i-1)/2]
        self.conStr = tmp
        print 'The result of sorting concatenate string is: ', self.conStr

    def qsort(self,a,st,ed):
        if st>=ed: return
        i, j, mid = st, ed, a[st]
        while i<j:
            while i<j and a[j]>mid: j = j-1
            if i<j: a[i] = a[j]
            while i<j and a[i]<mid: i = i+1
            if i<j: a[j] = a[i]
        a[i]=mid
        self.qsort(a,st,i-1)
        self.qsort(a,i+1,ed)

    def translateString(self):
        tmpStr, lowerStr = '', str.lower(self.conStr)
        for c in lowerStr:
            binStr = ''
            if c >= '0' and c <= '9':
                binStr = bin(ord(c)-ord('0'))
            if c >= 'a' and c <='f':
                binStr = bin(ord(c)-ord('a')+10)
            binStr = binStr[2:]
            binStr = (4-len(binStr))*'0'+binStr
            binStr = '0b'+binStr[::-1]
            tmpStr += str.upper(hex(int(binStr,2))[2])
        self.conStr = tmpStr
        print 'The result of translating concatenate string is: ',self.conStr



if __name__ == '__main__':

    s = Solution("dec","fab")
    s.concatenateString()
    s.sortString()
    s.translateString()

            

