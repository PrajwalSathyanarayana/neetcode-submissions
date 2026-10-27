class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 0 # 2 pointers
        for r in range(len(nums)): # iterate with r pointer over the entire array
            if nums[r]: # if current value is not 0 => swap and move left pointer
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            
# 0,0,1,2,0,5
# l = 0; r = 0;
#
# r = 0, l = 0, nums[r] == 0 => do nothing
# r = 1, l = 0, nums[r] == 0 => do nothing
# r = 2, l = 0, nums[r] == 1 => 0,1 = 1,0; l = 1; nums = 1,0,0,2,0,5
# r = 3, l = 1, nums[r] == 2 => 0,2 = 2,0; l = 2; nums = 1,2,0,0,0,5
# r = 4, l = 2, nums[r] == 0 => do nothing
# r = 5, l = 2, nums[r] == 5 => 0,5 = 5,0; l = 3; nums = 1,2,5,0,0,0
# r = 6, exit 
# nums = 1,2,5,0,0,0