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

#         0 1 2 3
# nums = [1,0,1,2]
# l=0, r=3, i=0, 0<=3:T, 1==0:F, 1==2:F, i=1
# l=0, r=3, i=1, 1<=3:T, 0==0:T, swap(0,1), [0,1,1,2], l=1, i=2
# l=1, r=3, i=2, 2<=3:T, 1==0:F, 1==2:F, i=3
# l=1, r=3, i=3, 3<=3:T, 2==0:F, 2==2:T, swap(3,3), [0,1,1,2], i=2, r=2, i=3
# l=1, r=2, i=3, 3<=2:F
# nums = [0,1,1,2]