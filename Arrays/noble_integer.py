class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        n = len(A)
        for i in xrange(n-1):
            if A[i+1] > A[i] and A[i] == n-1-i:
                return 1
       
        if A[n-1] == 0:
            return 1
        return -1
