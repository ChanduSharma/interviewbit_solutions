class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        
        n = len(A)
        
        low = 0
        high = n - 1
        result1 = -1
        
        while low <= high:
            mid = (low + high)//2
            
            if A[mid] == B:
                result1 = mid
                high = mid -1
            
            elif A[mid] > B:
                high = mid - 1
            else:
                low = mid + 1
        
        low = result1
        high = n - 1
        result2 = -1
        while low <= high:
            mid = (low + high)//2
            
            if A[mid] == B:
                result2 = mid
                low = mid + 1
            
            elif A[mid] > B:
                high = mid - 1
            else:
                low = mid + 1
                
        return [result1,result2]
