class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x # left and right pointer
        res = 0 # result is 0
        while l<=r: # pointer is in bound
            m = l + ((r-l)//2) # calculate mid
            if m**2 > x: # if mid^2 > x, search left half, r = mid - 1
                r = m-1
            elif m**2 < x: # if mid^2 , x, search right half, l = mid + 1
                l = m+1 
                res = m # m could potentially be result
            else:
                return m # return m since m^2 == x
        return res # if not, return res m^2 > or < x

# x = 13
# l=0, r=13, res=0
# 0<=13:yes, m=(0+6)=6, 36>13:yes, r=5, l=0
# 0<=5:yes, m=(0+2)=2, 4<13:yes, l=3, res=2, r=5
# 3<=5:yes, m=(3+1)=4, 16>13:yes, r=4, l=3, res=2
# 3<=4:yes, m=(3+0)=3, 9<13:yes, l=4, res=3, r=4
# 4<=4:yes, m=(4+0)=4, 16>13:yes, r=3, l=4, res=3
# 4<=3:no, return res=3