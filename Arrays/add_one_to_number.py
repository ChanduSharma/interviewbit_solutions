class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        tmp = []
        temp = 1
        
        for i in reversed(A):
            x = i + temp
            if x > 9:
                temp = 1
                tmp.append(x%10)
            else:
                tmp.append(x)
                temp = 0
        
        if temp:
            tmp.append(temp)
        tmp.reverse()
        l = 0
        for i in range(len(tmp)):
            if tmp[i] > 0:
                break
            else:
                l += 1
                
        return tmp[l:]

