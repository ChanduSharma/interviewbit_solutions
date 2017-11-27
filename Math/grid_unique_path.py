class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        ans = 1
        for i in xrange(B,A+B-1):
            ans *= i
            ans = ans//(i-B+1)
        
        return ans
