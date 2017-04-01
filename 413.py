class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        #pdb.set_trace()
        l = len(A)
        if l < 3:
            return 0
        f = [0 for i in range(l+1)]
        count = 0
        if A[1]-A[0] == A[2]-A[1]: 
            f[2] = 1
            count += 1
        for i in range(3,l):
        	if A[i]-A[i-1] == A[i-1]-A[i-2]:
        		f[i] = f[i-1] + 1
        	count += f[i]

        return count