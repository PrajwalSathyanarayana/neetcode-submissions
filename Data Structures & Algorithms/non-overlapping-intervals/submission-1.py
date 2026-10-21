class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i :i[0])
        result = 0 # result count
        prevEnd = intervals[0][1] # end value of first interval

        for start, end in intervals[1:]: # iterate from second interval
            if start >= prevEnd: # not overlapping; start value of current interval >= end value of previous interval # [1,3], [3,5] 3 >= 3
                prevEnd = end # update previous end to current end; prevEnd = 5
            else: # overlapping
                result += 1 # increase result by 1
                prevEnd = min(end, prevEnd) # update previous end to minimum between end value of current iteration and itself
            
        return result