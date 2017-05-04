#coding = utf-8
import sys

if __name__ == "__main__":
    num_dict = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}
    num_arr = []
    col_arr = []
    for i in range(5):
        num_c, color = sys.stdin.readline().strip().split(' ')
        num = num_dict[num_c]
        num_arr.append(num)
        col_arr.append(color)
    ans = 0

    if len(set(col_arr)) == 1:
        if min(num_arr)*5+10 == sum(num_arr): ans = 1
        else: ans = 4
    if not ans:
        if len(set(num_arr)) == 2:
            diff = list[set(num_arr)]
            tmp = [num_arr.count(diff[0]),num_arr.count(diff[1])]
            if max(tmp) == 4: ans = 2
            elif max(tmp) == 3: ans = 3
    if not ans:
        if min(num_arr)*5+10 == sum(num_arr): ans = 5
    if not ans:
        l = []
        for i in range(5):
            l.append(str(num_arr[i])+col_arr)
        if len(set(l)) == 3: ans = 6
    if not ans: ans = 7
    print ans 
