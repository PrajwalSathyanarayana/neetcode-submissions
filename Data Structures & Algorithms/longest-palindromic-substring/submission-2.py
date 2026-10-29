class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            #odd length
            l,r = i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1

            #even length
            l = i
            r = i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1
        
        return res

        # Input: s = "ababd"
# Initial: res = "", resLen = 0

# i = 0:
# Odd: l=0, r=0 → "a", length = 0-0+1 = 1
# 1 > 0 → res = "a", resLen = 1
# Expand: l=-1, r=1 → Out of bounds
# Even: l=0, r=1 → 'a' != 'b' → Stop

# i = 1:
# Odd: l=1, r=1 → "b", length = 1
# 1 > 1 → False, no update
# Expand: l=0, r=2 → "aba", length = 2-0+1 = 3
# 3 > 1 → res = "aba", resLen = 3
# Expand: l=-1, r=3 → Out of bounds
# Even: l=1, r=2 → 'b' != 'a' → Stop

# i = 2:
# Odd: l=2, r=2 → "a", length = 1
# 1 > 3 → False, no update
# Expand: l=1, r=3 → "bab", length = 3-1+1 = 3
# 3 > 3 → False, no update
# Expand: l=0, r=4 → 'a' != 'd' → Stop
# Even: l=2, r=3 → 'a' != 'b' → Stop

# i = 3:
# Odd: l=3, r=3 → "b", length = 1
# 1 > 3 → False, no update
# Expand: l=2, r=4 → 'a' != 'd' → Stop
# Even: l=3, r=4 → 'b' != 'd' → Stop

# i = 4:
# Odd: l=4, r=4 → "d", length = 1
# 1 > 3 → False, no update
# Expand: r=5 → Out of bounds
# Even: l=4, r=5 → Out of bounds

# Final: res = "aba", resLen = 3
# Output: "aba"