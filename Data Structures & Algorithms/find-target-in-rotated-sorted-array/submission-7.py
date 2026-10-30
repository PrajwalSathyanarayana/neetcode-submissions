class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:
            m = l + ((r-l)//2)

            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]: # left sorted
                if target>nums[m] or target<nums[l]:
                    l=m+1
                else:
                    r=m-1
            else: # right sorted
                if target<nums[m] or target>nums[r]:
                    r=m-1
                else:
                    l=m+1
        return -1

#         0 1 2 3 4 5
# nums = [3,4,5,6,1,2], target = 1
# l=0, r=5
# 0<=5:yes, m=2, 5==1:no, 3<=5:yes, 1>5 or 1<3:yes, l=3
# 3<=5:yes, m=4, 1==1:yes, return 4