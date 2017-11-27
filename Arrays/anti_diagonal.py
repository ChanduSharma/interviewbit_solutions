class Solution:
	# @param a : list of list of integers
	# @return a list of list of integers
	def diagonal(self, a):
	    n = len(a)
	    ans = [0] * (n * 2 - 1)
	    
	    for i in xrange(n*2 - 1):
	        ans[i] = []
	   
	   
	    for i in xrange(0,n):
	        for j in xrange(0,n):
	            ans[i+j].append(a[i][j])
	            
	    return ans
