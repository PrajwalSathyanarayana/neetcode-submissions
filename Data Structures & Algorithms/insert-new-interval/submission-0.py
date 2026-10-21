class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = [] # result array
        
        for i in range(len(intervals)): # iterate through intervals
            if newInterval[1] < intervals[i][0]: # end index of newInterval < start index of current interval => append the newInterval to result
                res.append(newInterval)
                return res + intervals[i:] # append the remaining intervals to result and return them
            
            elif newInterval[0] > intervals[i][1]: # start index of newInterval > end index of current interval => append the start index of current interval
                res.append(intervals[i])
            
            else: # newInterval over lapping with current interval
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            
        res.append(newInterval) # add the newInterval to the result
        return res # return result