class Solution:
    def numDecodings(self, s: str) -> int:
        
        # Recursive Caching approach

        dp = {len(s): 1} # hashmap; entire length of string mapped to 1

        def dfs(i): # recursive dfs with current position in the string
            if i in dp: # if current character is alreadyy cached or in last position in the string
                return dp[i]
            
            if s[i] == '0': # if the string starts with 0, return 0
                return 0
            
            res = dfs(i+1) # dfs for single digit

            if i+1 < len(s) and (
            (s[i] == '1') or # checking the condition for double digit
            (s[i] == '2' and s[i+1] in '0123456')): # between 10 - 26
                res += dfs(i+2) # dfs for doubule digit

            dp[i] = res # cache the result 

            return res # return the result
        
        return dfs(0) 