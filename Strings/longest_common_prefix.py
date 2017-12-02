class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        
        minlength = min(len(i) for i in A)
        n = len(A)
        result = []
        for i in xrange(minlength):
            temp = A[0][i]
            
            k = 1
            
            while k < n:
                if temp == A[k][i]:
                    k += 1
                else:
                    return ''.join(result)
            
            result.append(temp)
            
        return ''.join(result)
