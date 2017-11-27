from fractions import gcd
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cpFact(self, A, B):
        while gcd(A,B) != 1:
            A /= gcd(A,B)
            
        return A
