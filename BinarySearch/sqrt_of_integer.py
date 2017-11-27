class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        low = 0
        high = A
        mid = 0
        if A == 0 or A == 1:
            return A
        ans = 1
        while low <= high:
            mid = (low + high)//2
            if mid*mid == A:
                return mid
            elif mid*mid < A:
                low = mid + 1
                ans = mid
            else:
                high = mid - 1
        
        return ans
