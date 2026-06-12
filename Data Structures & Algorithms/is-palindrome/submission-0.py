class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = [i for i in s if i.isalnum()]
        s1 = "".join(clean_s)
        s1 = s1.casefold()
        return s1 == s1[::-1] 