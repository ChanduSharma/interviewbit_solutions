class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        
        while A > 0 and B > 0:
            A,B = B%A,A
        
        if A == 0:
            return B
        return A
