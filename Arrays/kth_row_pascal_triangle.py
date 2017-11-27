class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        ans = []
        c = 1
        ans.append(c)
        
        for i in range(1,A+1):
                c  = c * (A+1 - i)//i
                ans.append(c)
                
        return ans
