class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # 2 pointers left and right initialized to 1 and max value of piles
        res = r # result is max value of piles for now

        while l<=r: # pointers in bound
            k = (l+r)//2 # find the middle
            hours = 0 # track hours
            for p in piles: # iterate through the given piles array
                hours += math.ceil(p/k) # round up the no. of hours calculated
            if hours <= h:
                res = min(k,res) # update result
                r = k-1 # search left half; current k is high, find lower
            else: # search right half; current k is small, find higher
                l = k+1
        return res

# piles = [1,4,3,2] h=9
# l=1, r=4
# 1<=4:yes, k=(1+4)//2=2, hours=0, 
#           p=1, hours=0+1=1, 
#           p=4, hours=1+2=3, 
#           p=3, hours=3+2=5,
#           p=2, hours=5+1=6
#       6<=9:yes, res=min(2,6)=2; r=1
# 1<=1:yes, k=(1+1)//2=1, hours=0
#           p=1, hours=0+1=1,
#           p=4, hours=1+4=5,
#           p=3, hours=5+3=8,
#           p=2, hours=8+2=10
#       10<=9:no, l=2
# 2<=1:no, return res=2

