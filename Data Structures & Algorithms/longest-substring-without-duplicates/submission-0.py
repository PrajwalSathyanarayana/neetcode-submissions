class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        d = {}
        max_length = 0
        for char in s:
            if char in d:
                if d[char] >= l:
                    l = d[char] + 1
            d[char] = r                
            length = r - l + 1
            max_length = max(max_length, length)
            r += 1

        return max_length