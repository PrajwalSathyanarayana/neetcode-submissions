class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = res = 0 # left pointer and max window set to 0
        for r in range(len(nums)): # iterate through the input
        # k tracks the number of zeroes allowed to flip in current window
            k -= (1 if nums[r]==0 else 0) # increase k while expanding the current window
            while k<0: # while number of zeroes allowed to flip is less than 0
                k += (1 if nums[l]==0 else 0) # decrease k while shrinking current window
                l += 1 # move left pointer inward
            res = max(res, r-l+1) # max value of the current window
        return res # return result