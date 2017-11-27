class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        sign = 1
        if A < 0:
            sign = -1
            
        tmp = str(sign*A)
        
        num = sign * int(tmp[::-1])
        
        if num <= 2**31 - 1 and num >= -(2**31-1):
            return num
        
        return 0
