import collections
class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        choices = collections.deque(range(1, B + 1))

        next_is_smaller = lambda c : c == 'D'

        next_is_greater = lambda c : c == 'I'
        ans = []
        for condition in A:
            if next_is_smaller(condition):
                ans.append(choices.pop())
            elif next_is_greater(condition):
                ans.append(choices.popleft())

        ans.append(choices.pop())
        return ans
