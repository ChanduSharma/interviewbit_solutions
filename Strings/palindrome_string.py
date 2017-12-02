class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        
        tmp = []
        
        for i in A:
            if i.isalnum():
                tmp.append(i)
                
        tmp = ''.join(tmp)
        tmp = tmp.lower()
        return 1 if tmp == tmp[::-1] else 0
