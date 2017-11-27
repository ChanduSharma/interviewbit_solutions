class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        temp = sorted(A)
        k = 1
        count = 0
        for i in temp:
            if i < 0:
                count += 1
        
        if count == len(temp):
            return k
        
        for i in temp:
            if i > 0:
                if i == k:
                    k += 1
                else:
                    return k
        
        if len(temp) == k-1:
            return k
