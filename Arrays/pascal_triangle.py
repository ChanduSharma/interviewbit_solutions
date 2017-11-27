class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        ans  = []
        for line in range(1,A+1):
            l = []
            c = 1
            l.append(c)
            
            for i in range(1,line):
                c  = c * (line - i)//i
                l.append(c)
        
            ans.append(l)
        
        return ans
