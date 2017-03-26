class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = []
        ln = []
        sn = []
        if len(num1) >= len(num2):
            for c in reversed(num1):
                ln.append(int(c))
            for c in reversed(num2):
                sn.append(int(c))
            for i in range(len(sn),len(ln)):
                sn.append(0)
        else:
            for c in reversed(num1):
                sn.append(int(c))
            for c in reversed(num2):
                ln.append(int(c))
            for i in range(len(sn),len(ln)):
                sn.append(0)
            
        next = 0
        for i in range(len(ln)):
            ans.append((sn[i]+ln[i]+next)%10)
            next = (sn[i]+ln[i]+next)/10
        if next:
            ans.append(next)
        ansStr = ''
        for v in reversed(ans):
            ansStr += str(v)
        return ansStr
        
        