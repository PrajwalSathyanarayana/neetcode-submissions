class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        char = set()
        res = 0

        for r in range(len(s)):
            while s[r] in char:
                char.remove(s[l])
                l += 1
            char.add(s[r])
            res = max(res, r-l+1)
        return res

# l = 0, char = (), res = 0, len(s) = 7 "zxyzxyz", r: 0 to 6

# r = 0, s[0] in char: no, add z, char = (z), res = max(0,0-0+1) = 1
# r = 1, s[1] in char: no, add x, char = (z,x), res = max(1,1-0+1) = 2
# r = 2, s[2] in char: no, add y, char = (z,x,y), res = max(2,2-0+1) = 3
# r = 3, s[3] in char: yes, remove s[0] = z, l = 1, s[3](z) in char: no, add z,
# char = (x,y,z), res = max(3,3-1+1) = 3
# r = 4, s[4](x) in char: yes, remove s[1] = x, char = (y,z), l = 2, s[4](x) in char: no, add x, 
# char = (y,z,x), res = max(3,4-2+1) = 3
# r = 5, s[5](y) in char: yes, remove s[2] = y, char = (z,x), l = 3, s[5](y) in char: no, add y
# char = (z,x,y), res = max(3,5-3+1) = 3
# r = 6, s[6](z) in char: yes, remove s[3] = z, char = (x,y), l = 4, s[6](z) in char: no, add z
# char = (x,y,z), res = max(3,6-4+1) = 3, return 3