class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        m = len(matrix)
        if m:
            n = len(matrix[0])
        else:
            return []
        rows = [[] for i in range(0,(n-1)+(m-1)+1)]
        for i in range(0,m):
            for j in range(0,n):
                rows[i+j].append([i,j])
        flag = 0
        for row in rows:
            if flag == 0:
                row = sorted(row,key=lambda x:x[0],reverse = True)
                for x in row:
                    ret.append(matrix[x[0]][x[1]])
                flag = 1
            elif flag == 1:
                row = sorted(row,key=lambda x:x[0])
                for x in row:
                    ret.append(matrix[x[0]][x[1]])
                flag = 0

        return ret