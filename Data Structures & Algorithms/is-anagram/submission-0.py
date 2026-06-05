from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        else:
            s_c = Counter(s)
            t_c = Counter(t)
            if s_c == t_c: return True
            else: return False