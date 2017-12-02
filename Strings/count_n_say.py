class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        
        if A == 1:
            return '1'
        if A == 2:
            return '11'
            
        ml = ['1','1']
        
        for i in xrange(3,A+1):
            
            ml.append('#')
            
            length = len(ml)
            
            count = 1
            tmp = []
            
            for j in xrange(1,length):
                
                if ml[j] != ml[j-1]:
                    tmp.append(str(count))
                    tmp.append(ml[j-1])
                    count = 1
                else:
                    count += 1
                
            ml = tmp
            
        return ''.join(ml)
