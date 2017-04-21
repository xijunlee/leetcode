#coding = utf-8
import sys

if __name__ == "__main__":
    m, n = sys.stdin.readline().strip().split(' ')
    m, n = int(m), int(n)
    a = []
    for i in xrange(m):
        line = sys.stdin.readline().strip().split(' ')
        tmp = []
        for v in line:
            tmp.append(int(v))
        a.append(tmp)
    f = []
    for i in range(m):
        f.append([0 for j in range(n)])
    for i in range(m):
        for j in range(n):
            if j-1 >= 0: f[i][j] = max(f[i][j],f[i][j-1])
            if i-1 >= 0: f[i][j] = max(f[i][j],f[i-1][j])
            f[i][j] += a[i][j]
    print f[m-1][n-1]