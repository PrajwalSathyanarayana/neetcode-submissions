"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals]) # start values in an array in ascending order
        end = sorted([i.end for i in intervals]) # end values in an array in descending order

        result,count = 0,0 # result = max(result, count); count to keep track of meeting rooms
        s,e = 0,0 # 2 pointers

        while s<len(intervals):
            if start[s] < end[e]:
                s += 1; count += 1
            else:
                e += 1; count -= 1
            result = max(result, count)
        
        return result