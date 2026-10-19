class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        for n in nums:
            temp = max(rob1 + n, rob2) # [rob1, rob2, n, n+1, n+2, .....] either rob rob1+n or rob rob2
            rob1 = rob2 # update rob1 to rob2
            rob2 = temp # update rob2 to n
        
        return rob2