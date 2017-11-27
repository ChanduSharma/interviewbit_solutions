class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        start = end = 0
        s = 0
        cmax = 0
        tmax = -99999999999999999
        ans = 0
        tmp = []
        tmp += A
        count = 0
        tmp = map(int,tmp)
        
        i = 0
        while i < len(tmp):
            if tmp[i] == 0:
                tmp[i] = 1
            else:
                tmp[i] = -1
                count += 1
           
            cmax += tmp[i]
            if cmax > tmax:
                tmax = cmax
                start = s
                end = i
            if cmax < 0:
                cmax = 0
                s = i + 1
            
            i += 1
        if len(tmp) == count:
            return []
        return [start+1,end+1]
