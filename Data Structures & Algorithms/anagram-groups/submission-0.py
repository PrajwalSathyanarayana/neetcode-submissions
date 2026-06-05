class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            k = "".join(sorted(i))
            if k not in d:
                d[k] = [i]
            else:
                d[k].append(i)
        return list(d.values())