def isprime(n):
    if n == 2 or n== 3:
        return True
    if n%2 == 0 or n < 2:
        return False
    i = 3
    while i*i <= n:
        if n%i == 0:
            return False
        i += 2
        
    return True
class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        for i in xrange(2,A+1):
            if isprime(i) and isprime(A-i):
                return [i,A-i]
