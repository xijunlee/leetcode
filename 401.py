class Solution(object):
    def readBinaryWatch(self, num):
        ret = []
        if num == 0:
            ret.append('0:00')
            return ret

        for i in range(1024):
            count = 0
            n = i
            while n:
                n = n&(n-1)
                count += 1
            if count == num:
                high = (i & (15 << 6)) >> 6
                low = i & 63
                if high < 12 and low < 10:
                    ret.append(str(high)+':0'+str(low))
                elif high < 12 and low < 60:
                    ret.append(str(high)+':'+str(low))
        return ret
        