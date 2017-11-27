class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        tmp = A
        tmp.sort()
        
        for i in xrange(0,len(tmp)-1,2):
            tmp[i],tmp[i+1] = tmp[i+1],tmp[i]
            
        return tmp
