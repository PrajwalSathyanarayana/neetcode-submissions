class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        # ans = []
        for i in nums:
            d[i] = 1 + d.get(i,0)
        d = sorted(d, key=d.get, reverse = True)
        # for i in d:
        #     ans.append(i[0])
        return d[:k]