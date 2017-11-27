class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        m = len(A)
        n = len(A[0])
        rows = list()
        coloumns = set()
        for row in xrange(m):
            x = 1
            for col in xrange(n):
                x &= A[row][col]
                if A[row][col] == 0:
                    coloumns.add(col)
                    
            if x == 0:
                rows.append(row)
        
        for row in rows:
            for col in xrange(n):
                A[row][col] = 0
            
        for col in coloumns:
            for row in xrange(m):
                A[row][col] = 0
            
        return A
