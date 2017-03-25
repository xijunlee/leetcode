#coding = utf-8
import sys
import pdb

if __name__ == "__main__":
    
    line = sys.stdin.readline()
    nk = map(int, line.strip().split())
    n,k = nk[0],nk[1]
    line = sys.stdin.readline()
    values = map(int, line.strip().split())
    #pdb.set_trace()
    for s in range(k):
        ori = values[:]
        for i in range(n):
            if i < n-1:
                values[i]=(ori[i]+ori[i+1])%100
            else:
                values[i]=(ori[i]+ori[0])%100
    ans = ""
    for i in range(n-1):
        ans += str(values[i])+ " "
    ans += str(values[n-1])
    print ans