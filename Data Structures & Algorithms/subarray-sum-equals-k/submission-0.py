class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 # result
        curSum = 0 # current curSum
        prefixSum = {0: 1} # hashmap with empty sub array

        for n in nums: # iterate through the input
            curSum += n
            diff = curSum - k
            res += prefixSum.get(diff,0)
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)

        return res
