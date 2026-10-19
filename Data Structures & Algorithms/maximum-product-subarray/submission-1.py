class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1, 1

        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
                continue
            
            temp1 = curMax * n
            temp2 = curMin * n

            curMax = max(temp1, temp2, n)
            curMin = min(temp1, temp2, n)

            res = max(res, curMax, curMin)
        
        return res