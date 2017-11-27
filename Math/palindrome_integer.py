class Solution:
    # @param A : integer
    # @return a boolean value ( True / False )
    def isPalindrome(self, A):
        tmp = str(A)
        return tmp == tmp[::-1]
