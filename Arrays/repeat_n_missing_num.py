class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        frequency_table =[0]*(len(A)+1)
        repeated = missing = 0
        
        for number in A:
            frequency_table[number] += 1
            
        for i in range(1,len(frequency_table)):
            if frequency_table[i] == 0:
                missing = i
            if frequency_table[i] == 2:
                repeated = i
                
        return [repeated,missing]
