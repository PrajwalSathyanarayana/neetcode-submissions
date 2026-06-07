class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        n = len(nums)
        ans = []
        buckets = [[] for _ in range(n+1)]
        for i in nums:
            d[i] = 1 + d.get(i, 0)
        for element, freq in d.items():
            buckets[freq].append(element)
        for bucket in buckets[::-1]:
            for element in bucket:
                ans.append(element)
                if len(ans) == k:
                    return ans