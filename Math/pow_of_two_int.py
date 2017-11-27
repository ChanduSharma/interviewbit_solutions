class Solution:
    # @param A : integer
    # @return a boolean
    def isPower(self, A):
        if A == 1:
            return True
        i = 2
        while i*i <= A:
            p = i
            while p <= A:
                p *= i
                if p == A:
                    return True
            
            i += 1
        
        return False
