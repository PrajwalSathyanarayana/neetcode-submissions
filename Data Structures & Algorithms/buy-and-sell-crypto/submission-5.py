class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
            else:
                l = r
            r += 1

        return maxP

# [10,1,5,6,7,1]
# l = 0, r = 1, maxP = 0
# 1<6: yes, 10<1: no, l = r = 1, r = 2
# 2<6: yes, 1<5: yes, profit = 5-1 = 4, maxP = max(4,0) = 4, r = 3, l = 1
# 3<6: yes, 1<6: yes, profit = 6-1 = 5, maxP = max(5,4) = 5, r = 4, l = 1
# 4<6: yes, 1<7: yes, profit = 7-1 = 6, maxP = max(6,5) = 6, r = 5, l = 1
# 5<6: yes, 1<1: no, l = r = 5, r = 6,
# 6<6: no, return maxP = 6