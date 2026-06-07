class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        # ans = []
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] = d[i] + 1
        d = sorted(d, key=d.get, reverse = True)
        # for i in d:
        #     ans.append(i[0])
        return d[:k]