class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        result = 0
        i = len(A) - 1
        t = 0
        while i >= 0:
            result += (26**t) * (ord(A[i]) - ord('A') + 1)
            i -= 1
            t += 1
        
        return result
