class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l = curSum = 0
        target = sum(nums)-x
        max_window = -1

        for r in range(len(nums)):
            curSum += nums[r]

            while l<=r and curSum>target:
                curSum -= nums[l]
                l += 1
            
            if curSum == target:
                max_window = max(max_window, r-l+1)
        
        return -1 if max_window == -1 else len(nums)-max_window

#       0 1 2 3
# nums=[2,5,1,3], x=5
# l=0, curSum=0, max_window=-1, target=11-5=6
# l=0, r=0, curSum=0+2=2, 0<=0 and 2>6:False, 0==6:no, max_window=-1
# l=0, r=1, curSum=2+5=7, 0<=1 and 7>6:True, curSum=7-2=5, l=1, 1<=1 and 5>6:False, 5==6:no, max_window=-1
# l=1, r=2, curSum=5+1=6, 1<=2 and 6>6:False, 6==6:yes, max_window=max(-1,2)=2
# l=1, r=3, curSum=6+3=9, 1<=3 and 9>6:True, curSum=9-5=4, l=2, 2<=3 and 4>6:False, 4==6:False, max_window=2
# return len(nums)-max_window
# return 4-2 = 2