class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        
        pivot = 0
        low = 0
        n = len(A)
        high = n - 1
        
        while low <= high:
            if A[low] <= A[high]:
                pivot = low
                break
            
            mid = (low + high)//2
            next = (mid + 1)%n
            prev = (mid + n - 1)%n
            
            if A[mid] <= A[next] and A[mid] <= A[prev]:
                pivot = mid
                break
            elif A[mid] <= A[high]:
                high = mid - 1
            elif A[mid] >= A[low]:
                low = mid + 1
                
        if pivot == 0:
            low = 0
            high = len(A) - 1
            while low <= high:
                mid = (low + high)//2
                if A[mid] == B:
                    return mid
                elif A[mid] > B:
                    high = mid - 1
                else:
                    low = mid + 1
        else:
            
            low = 0
            high = pivot - 1
            while low <= high:
                mid = (low + high)//2
                if A[mid] == B:
                    return mid
                elif A[mid] > B:
                    high = mid - 1
                else:
                    low = mid + 1

            low = pivot
            high = len(A) - 1
            while low <= high:
                mid = (low + high)//2
                if A[mid] == B:
                    return mid
                elif A[mid] > B:
                    high = mid - 1
                else:
                    low = mid + 1

        return -1
