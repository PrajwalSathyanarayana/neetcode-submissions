"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key = lambda i :i.start) # sort intervals based on start values

        for i in range(1, len(intervals)): # iterate throuugh intervals starting from index 1
            i1 = intervals[i-1] # previous interval
            i2 = intervals[i] # current interval
            if i2.start < i1.end: # if start of current interval < end of previous interval
                return False
        
        return True