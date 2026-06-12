class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while l < r:
            if not s[l].isalnum() and l<r:
                l += 1 
            elif not s[r].isalnum() and l<r:
                r -= 1
            elif s[l].casefold() == s[r].casefold():
                l += 1
                r -= 1
            else:
                return False
        return True