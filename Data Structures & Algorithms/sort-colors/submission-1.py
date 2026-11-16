class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums)-1 # 2 pointers left and right
        i = 0 # variable to iterate through the input array

        def swap(i,j): # helper function to swap 2 values
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        
        while i<=r: # while pointer in bounds
            if nums[i]==0: # if value is 0, swap value at left pointer and current value, move left pointer inward
                swap(l,i); l+=1 
            elif nums[i]==2: # if value is 2, swap value at right pointer and current value, move right pointer inward
                swap(i,r); r-=1
                i-=1 # decrement i to negate the increment
            i+=1 # increment i