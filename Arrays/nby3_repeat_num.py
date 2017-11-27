class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        slot1 = 10000000000000
        slot2 = 10000000000000
        count1 = 0
        count2 = 0
        
        for i in A:
            if count1 > 0 and i == slot1:
                count1 += 1
            elif count2 > 0 and i == slot2:
                count2 += 1
            elif count1 == 0:
                slot1 = i
                count1 = 1
            elif count2 == 0:
                slot2 = i
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        count1 = count2 = 0
        for i in A:
            if i == slot1:
                count1 += 1
            if i == slot2:
                count2 += 1
            
            if count1 > len(A)//3:
                return slot1
            if count2 > len(A)//3:
                return slot2
                
        return -1
