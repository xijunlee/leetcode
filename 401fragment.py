'''
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ret=[]
        
        self.dfs(0,ret,num,0)
        
        return ret
        
    def dfs(self, step, ret, num, digital):
        if step >= 10:
            if num == 0:
               pdb.set_trace()
               print bin(digital)
               hstr = str((digital & (15<<8))>>8)
               print bin((digital & (15<<8))>>8)
               m = digital & 255
               print bin(m)
               if m < 10:
                   mstr = '0'+ str(m)
               else:
                   mstr = str(m)
               ret.append(hstr+':'+mstr)
               return 
            else:
               return
       
        self.dfs(step+1,ret,num,digital)
        if num-1 >= 0:
            self.dfs(step+1,ret,num-1,digital+(1<<step))
'''

