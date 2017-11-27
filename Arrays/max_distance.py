class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        n = len(A)
        
        la = [0] * n
        ra = [0] * n
        
        la[0] = A[0]
        
        for i in xrange(1,n):
            la[i] = min(A[i],la[i-1])
            
        ra[n-1] = A[n-1]
        
        for i in xrange(n-2,-1,-1):
            ra[i] = max(A[i],ra[i+1])
            
        i = j = 0
        mdiff = 0
        while j < n and i < n:
            
            if la[i] <= ra[j]:
                mdiff = max(mdiff,j-i)
                j += 1
            else:
                i += 1
                
        return mdiff
