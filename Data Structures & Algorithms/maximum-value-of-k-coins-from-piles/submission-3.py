class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [0]*(k+1)
        for pile in piles:
            prefix = [0]
            for coin in pile[:k]: prefix.append(prefix[-1]+coin)
            for count in range(k,0,-1):
                for take in range(1,min(count,len(prefix)-1)+1):
                    dp[count] = max(dp[count],dp[count-take]+prefix[take])
        return dp[k]
