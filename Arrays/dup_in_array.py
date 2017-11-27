class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        temp = list(A)
        ans = []
        for i in range(len(temp)):
            
            if temp[abs(temp[i])] >= 0:
                temp[abs(temp[i])] = -temp[abs(temp[i])]
            else:
                return abs(temp[i])
