class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        count = 0
        for i in A:
            if i < 0:
                count += 1
        
        if count == len(A):
            return []
        
        cmax = 0
        tmax = -1
        start = 0
        end = 0
        s = 0
        
        for i in range(len(A)):
            if A[i] >= 0:
                cmax += A[i]
                if cmax > tmax:
                    tmax = cmax
                    start = s
                    end = i
                
                if cmax == tmax:
                    if i-s > end-start:
                        start = s
                        end = i
                
            else:
                cmax = 0
                s = i + 1
                   
        return A[start:end+1]
