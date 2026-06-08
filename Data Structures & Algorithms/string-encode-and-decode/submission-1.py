class Solution:

    def encode(self, strs: List[str]) -> str:
        e = ""
        for i in strs:
            l = len(i)
            i = str(l) + "#" + i
            e += i
        return e
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            h = s.index('#', i)
            n = int(s[i:h])
            res.append(s[h+1:h+1+n])
            i = h+1+n
        return res
