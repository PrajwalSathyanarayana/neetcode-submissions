class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] # result array
        nums.sort() # sort the input array

        for i, a in enumerate(nums): # iterate through the input array
            if i>0 and a==nums[i-1]: # current index>0, and value is same as previous => continue
                continue
            l = i+1 # left pointer
            r = len(nums)-1 # right pointer

            while l<r: # while pointers are in bound
                threeSum = a + nums[l] + nums[r] # calculate the 3sum
                if threeSum > 0: # if 3sum > 0, move the right pointer inward
                    r -= 1
                elif threeSum < 0: # if 3sum < 0, then move the left pointer inward
                    l += 1
                else: # 3sum == 0, append the values into result array
                    res.append([a, nums[l], nums[r]])
                    l += 1 # increment left pointer
                    while nums[l] == nums[l-1] and l<r: # check if previous number and current number after incrementing left pointer is same and its in bound => then increment left pointer
                        l += 1
            
        return res

# nums = [-1,0,1,2,-1,-4]
# res = []
# nums = [-4,-1,-1,0,1,2]
# enumerate(nums) = {0: -4, 1: -1, 2: -1, 3: 0, 4: 1, 5: 2}
# i=0, a=-4, 0>0:False, dont skip, l=1, r=5, 
#            1<5:yes, threeSum=-4-1+2=-3, -3<0, l=2
#            2<5:yes, threeSum=-4-1+2=-3, -3<0, l=3
#            3<5:yes, threeSum=-4+0+2=-2, -2<0, l=4
#            4<5:yes, threeSum=-4+1+2=-1, -1<0, l=5
#            5<5:no, res = []
# i=1, a=-1, 1>0:True and -1!=-4:False, dont skip, l=2, r=5
#            2<5:yes, threeSum=-1-1+2=0, res=[[-1,-1,2]], l=3, 0==-1:no
#            3<5:yes, threeSum=-1+0+2=1, 1>0:yes, r=4
#            3<4:yes, threeSum=-1+0+1=0, res=[[-1,-1,2],[-1,0,1]], l=4, 1==0:no
#            4<4:no, res = [[-1,-1,2],[-1,0,1]]
# i=2, a=-1, 2>0:True and -1==-1:True, skip this iteration
# i=3, a=0, 3>0:True and 0==-1:False, dont skip it, l=4, r=5
#           4<5:yes, threeSum=0+1+2=3, 3>0, r=4
#           4<4:no, res = [[-1,-1,2],[-1,0,1]]
# i=4, a=1, 4>0:True and 1==0:False, dont skip it, l=5, r=5
#           5<5:no, res = [[-1,-1,2],[-1,0,1]]
# i=5, a=2, 5>0:True and 2==1:False, dont skip it, l=6, r=5
#           6<5:no, res=[[-1,-1,2],[-1,0,1]]
# return res = [[-1,-1,2],[-1,0,1]]