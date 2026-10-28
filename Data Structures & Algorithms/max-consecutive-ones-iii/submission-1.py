class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = res = 0 # left pointer and max window set to 0
        for r in range(len(nums)): # iterate through the input
        # k tracks the number of zeroes allowed to flip in current window
        # subtract 1 when 0 enters a window, add 1 when 0 leaves a window
            k -= (1 if nums[r]==0 else 0) # increase k while expanding the current window
            while k<0: # while number of zeroes allowed to flip is less than 0
                k += (1 if nums[l]==0 else 0) # decrease k while shrinking current window
                l += 1 # move left pointer inward
            res = max(res, r-l+1) # max value of the current window
        return res # return result

#  0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18   
# [0,0,1,1,0,0,1,1,1,0,1, 1, 0, 0, 0, 1, 1, 1, 1], k = 3
# l=0, res=0
# r=0; k=3-1=2; 2<0:no; res=max(0,1)=1; l=0;
# r=1; k=2-1=1; 1<0:no; res=max(1,2)=2; l=0;
# r=2; k=1-0=1; 1<0:no; res=max(2,3)=3; l=0;
# r=3; k=1-0=0; 1<0:no; res=max(3,4)=4; l=0;
# r=4; k=1-1=0; 0<0:no; res=max(4,5)=5; l=0;
# r=5; k=0-1=-1; -1<0:yes, 
#      k=-1+1=0, l=1, 0<0:no; res=max(5,5)=5; l=1;
# r=6; k=0-0=0; 0<0:no; res=max(5,6)=6; l=1;
# r=7; k=0-0=0; 0<0:no; res=max(6,7)=7; l=1;
# r=8; k=0-0=0; 0<0:no; res=max(7,8)=8; l=1;
# r=9; k=0-1=-1; -1<0:yes, 
#      k=-1+1=0, l=2, 0<0:no; res=max(8,8)=8; l=2;
# r=10; k=0-0=0; 0<0:no; res=max(8,9)=9; l=2;
# r=11; k=0-0=0; 0<0:no; res=max(9,10)=10; l=2;
# r=12; k=0-1=-1; -1<0:yes, 
#       k=-1+0=-1, l=3, -1<0:yes, 
#       k=-1+0, l=4, -1<0:yes, 
#       k=-1+1=0, l=5, 0<0:no; res=max(10,8)=10; l=5;
# r=13; k=0-1=-1, -1<0:yes, 
#       k=-1+1=0, l=6, 0<0:no; res=max(10,5)=10, l=6
# r=14; k=0-1=-1, -1<0:yes, 
#       k=-1+0=-1, l=7, -1<0:yes, 
#       k=-1+0=-1, l=9, -1<0:yes, 
#       k=-1+1=0, l=10, 0<0:no; res=max(10,5)=10; l=10
# r=15; k=0-0; 0<0:no; res=max(10,6)=10; l=10;
# r=16; k=0-0; 0<0:no; res=max(10,7)=10; l=10;
# r=17; k=0-0; 0<0:no; res=max(10,8)=10; l=10;
# r=18; k=0-0; 0<0:no; res=max(10,9)=10; l=10;
# return res 10