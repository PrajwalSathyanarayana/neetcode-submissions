class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums) # creating a hashset
        l = 0 # length of longest sequence

        for n in nums: # iterate through the array
            if (n-1) not in nset: # if the previous element not in set, then start of sequence
                length = 0 # variable to keep track of the length of current sequence
                while (n + length) in nset: # if the consecutive element in set
                    length += 1 # increment current length of sequuuence by 1
                l = max(l, length)  # max length
        
        return l