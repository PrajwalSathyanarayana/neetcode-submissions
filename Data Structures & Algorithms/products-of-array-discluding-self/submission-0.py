class Solution:
        def productExceptSelf(self, nums: List[int]) -> List[int]:
            res = []
            for i in range(len(nums)):
                c = 1
                for j in range(len(nums)):
                    if i == j:
                        continue
                    else:
                        c = c*nums[j]
                res.append(c)
            return res