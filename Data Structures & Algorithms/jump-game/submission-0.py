class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1 # pointer variable

        for i in range(len(nums)-1, -1, -1): # iterate from right to left (reverse direction)
            if i + nums[i] >= goal: # if the jump starting from position i exceeds goal, then move goal closer to i
                goal = i
        
        return True if goal == 0 else False # if goal is at position 0, return True