#calculating the maximum contiguous subarray within an array which has the largest sum.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        cmax = A[0]
        tmax = A[0]
        for i in A[1:]:
            cmax = max(i,cmax+i)
            tmax = max(cmax,tmax)
        return tmax
