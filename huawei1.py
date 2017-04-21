#coding = utf-8
import sys

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    year, month, day = line.split('-')
    year, month, day = int(year), int(month), int(day)
    day_of_month_0 = [31,28,31,30,31,30,31,31,30,31,30,31]
    day_of_month_1 = [31,29,31,30,31,30,31,31,30,31,30,31]

    check = True
    if year >= 10000: check = False
    if month > 12: check = False
    if day_of_month_1[month-1] < day: check = False

    if check == False: print "invalid input"
    else:
    	flag, ans = 0, 0
    	if year % 4 == 0 and year % 100 != 0: flag = 1
    	if year % 400 == 0: flag = 1
    	if flag == 0:
    		for i in range(0,month-1):
    			ans += day_of_month_0[i]
    		ans += day
    	if flag == 1:
    		for i in range(0,month-1):
    			ans += day_of_month_1[i]
    		ans += day
    	print line+" is the No."+str(ans)+" day of "+str(year)


    