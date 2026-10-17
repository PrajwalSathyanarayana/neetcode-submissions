class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] # list to store result
        
        def dfs(i, cur, total): # helper function with pointer i, current value cur, sum total
            if total == target: # if total is equal to target
                res.append(cur.copy()) # append the cop of current value, since current value would be used ahead
                return
            if ((i >= len(nums)) or (total > target)): # if the pointer is out of bound or sum total exceeds target value 
                return
            
            # Decision 1: include the cur value
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()

            # Decision 2: recursive call to dfs
            dfs(i+1, cur, total)

        dfs(0,[],0)

        return res