class Solution:
    def countBits(self, n: int) -> List[int]:
        
        dp = [0] * (n+1) # dp array initialized to 0 of length n

        offSet = 1 # highest power of 2

        for i in range(1, n+1):
            if offSet * 2 == i: # check if offset can be doubled
                offSet = i
            dp[i] = 1 + dp[i - offSet]
        
        return dp