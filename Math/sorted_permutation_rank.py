class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        n = len(A)
        ml = math.factorial(n)
        rank = 1
        for i in xrange(n):
            ml /= n - i
            count = 0
            p = 1
            for j in xrange(i+1,n):
                if A[j] <= A[i]:
                    if A[j] == A[i]:
                        p+=1
                    count += 1
            
            rank += count * ml//math.factorial(p)
            
        return rank%1000003
            
