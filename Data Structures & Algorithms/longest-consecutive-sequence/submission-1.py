class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        longest = 0
        for i in n:
            if i-1 not in n:
                length = 1
                while (i+length) in n:
                    length += 1
                longest = max(longest, length)
        return longest