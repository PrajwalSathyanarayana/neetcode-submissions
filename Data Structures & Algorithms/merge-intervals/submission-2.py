class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0]) # sort intervals by start time
        output = [intervals[0]] # output list with the first interval

        for s,e in intervals[1:]: # iterate through each interval in sorted list
            lastEnd = output[-1][1] # last interval in output
            if s<=lastEnd: # if current interval overlaps with last interval
                output[-1][1] = max(lastEnd, e) # merge them by updatinf the end
            else: # no overlap
                output.append([s,e]) # append the current interval to output as new interval
        return output # return output

# intervals = [[1,3],[1,5],[6,7]]
# intervals = [[1,3],[1,5],[6,7]] # after .sort
# output = [[1,3]]

# s=1, e=5, lastEnd=3, 1<=3:yes, output[-1][1]=max(3,5)=5, output=[[1,5]]
# s=6, e=7, lastEnd=5, 6<=5:no, output=[[1,5],[6,7]]
# return output [[1,5],[6,7]]