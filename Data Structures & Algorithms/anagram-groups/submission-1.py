class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            w_s = tuple(sorted(i))
            if w_s not in d:
                d[w_s] = [i]
            else:
                d[w_s].append(i)
        return list(d.values())