def comparestr(s1,s2):
    x =  s1+s2
    y = s2+s1
    if x > y:
        return 1
    elif x < y:
        return -1
    return 0
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        myl = list(map(str,A))
        myl.sort(cmp = comparestr,reverse = True)
        return int(''.join(myl))
