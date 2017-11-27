class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        arrive.sort()
        depart.sort()
        n = len(arrive)
        rooms_needed = 1
        i = 1
        j = 0
        while i < n and j < n:
            if arrive[i] < depart[j]:
                rooms_needed += 1
                i += 1
                if rooms_needed > K:
                    return 0
            else:
                rooms_needed -= 1
                j += 1
            
        return 1
