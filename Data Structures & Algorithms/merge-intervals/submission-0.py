class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0]) # sorting a list of pairs by start value
        output = [intervals[0]] # output list initialized with first interval 

        for start, end in intervals[1:]: # iterate through intervals starting from intervals[1:], since intervals[0] was added to output
            lastEnd = output[-1][1] # end value of the most recently added interval

            if start <= lastEnd: # intervals overlap => merge 
                output[-1][1] = max(lastEnd, end) # most recently added interval value; ending value is max between itself and the current end value; # [1,5],[2,4] = [1,5]
            else: # add interval to output
                output.append([start, end]) # [1,5],[7,8] = [1,5],[7,8]
        
        return output
            
                