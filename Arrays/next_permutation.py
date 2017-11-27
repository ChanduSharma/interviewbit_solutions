class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        n = len(A) - 1
        
        while n > 0 and A[n-1] >= A[n]:
            n -= 1
        
        if n <= 0:
            return reversed(A)
        
        j = len(A) - 1
        
        while A[j] < A[n-1]:
            j -= 1
        
        A[n-1],A[j] = A[j],A[n-1]
        
        j = len(A) - 1
        
        while n < j:
            A[n],A[j] = A[j],A[n]
            n += 1
            j -= 1
        
        return A
