class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1 # 2 pointer variables
        
        for i in range(n-1):
            temp = one # store copy of one in temp
            one = one + two # add one and two
            two = temp # swap one and two

        return one