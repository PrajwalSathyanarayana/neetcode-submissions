class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            subarrays = 0 # no. of sub arrays
            curSum = 0 # current sum
            for n in nums: # iterate through input
                curSum += n # calculate current sum through each value in input
                if curSum > largest: # current sum exceeds largest, then create new sub array starting from n
                    subarrays += 1
                    curSum = n
            return subarrays + 1 <= k

        l = max(nums) # left pointer with max input value
        r = sum(nums) # right pointer with sum of input values
        res = r # assum result to be sum of nums

        while l<=r:
            mid = l + ((r-l)//2) # calculate mid
            if canSplit(mid): # helper function with mid as largest value
                res = mid # if true, then update result with current mid
                r = mid - 1 # update right pointer to mid-1
            else:
                l = mid + 1 # update left pointer to mid+1
        return res