class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        A = zip(*A[::-1])
        return A
