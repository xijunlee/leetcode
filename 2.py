#coding = utf-8
import sys
import pdb

if __name__ == "__main__":
    
    line = sys.stdin.readline()
    s = str(line.strip())
    line = sys.stdin.readline()
    n = int(line.strip())
    k = 0
    pos = []
    
    s = list(s)
    for i in range(len(s)):
        if s[i] == 'X':
            k += 1
            pos.append(i)
    ret = 0
    for v in range(10 ** k):
        l = []
        tmp = v
        while tmp>0:
            l.append(tmp%10)
            tmp/=10
        for i in range(len(l),len(pos)):
            l.append(0)
        
        l = str(l[i])
        l = list(l)
        for i in range(len(pos)):
            s[pos[i]] = l[i]
        
        trans = ''
        for c in s:
            trans += c


        num = int(trans)
        if num % n == 0:
            print num
            
            ret += 1

    print ret

