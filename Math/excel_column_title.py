class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        ans = []
        while A > 0:
            val = A%26 
            if not val:
                ans.append('Z')
                A = A//26 -1
            else:
                ans.append(chr(val -1 + ord('A')))
                A = A//26
        
        return ''.join(reversed(ans))
