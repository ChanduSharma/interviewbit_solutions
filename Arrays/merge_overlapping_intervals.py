# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
from operator import attrgetter
class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        temp = intervals[:]
        temp = sorted(temp,key = attrgetter('start','end'))
        
        ans = []
        ans.append(Interval(temp[0].start,temp[0].end))
        for i in range(1,len(temp)):
            tmp = ans.pop()
            if temp[i].start >= tmp.start and temp[i].start <= tmp.end:
                ans.append( Interval(tmp.start,max(temp[i].end,tmp.end)) )
            else:
                ans.append(tmp)
                ans.append(Interval(temp[i].start,temp[i].end))
                
        return ans
