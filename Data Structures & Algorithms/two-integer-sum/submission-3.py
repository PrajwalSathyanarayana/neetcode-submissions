class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {} # hashmap
        for i, num in enumerate(nums): # iterate through the list of indices,value
            diff = target - num # find the difference between target and the current value
            if diff in d:
                return [d[diff],i]
            d[num] = i