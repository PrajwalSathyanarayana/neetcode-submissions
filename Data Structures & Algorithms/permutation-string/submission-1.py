class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        n = len(s1)

        for i in range(len(s2) - n + 1):
            subStr = s2[i:i+n]

            if sorted(subStr) == s1:
                return True

        return False 