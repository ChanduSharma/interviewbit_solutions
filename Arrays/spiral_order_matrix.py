class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        if A == 1:
            return [[1,]]
        l =[[0 for i in range(A)] for j in range(A)]
        k = 1
        top = 0
        left = 0
        right = A-1
        bottom = A-1
        n = A*A
        while k <= n:
            i = left
            while i <= right:
                l[top][i] = k
                k += 1
                i += 1
            
            top += 1
            
            i = top
            while i <= bottom:
                l[i][right] = k
                k += 1
                i += 1
                
            right -= 1
            
            i = right
            while i >= left:
                l[bottom][i] = k
                k += 1
                i -= 1
            
            bottom -= 1
            
            i = bottom
            while i >= top:
                l[i][left] = k
                k += 1
                i -= 1
            
            left += 1
                
        return l
