class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0 # result count

        for i in range(len(s)): # iterate through every single character in string s

            # odd length strings
            l, r = i, i # initialize 2 pointers left and right
        
            while ((l>=0) and (r<len(s)) and (s[l] == s[r])): # check if the pointers are in bound and character at pointer l == character at pointer r
                res += 1 # increment count of result
                l -= 1 # move left pointer to left
                r += 1 # move right pointer to right
        
            # even length strings    
            l, r = i, i+1 # initialize 2 pointers left and right
        
            while ((l>=0) and (r<len(s)) and (s[l] == s[r])): # check if the pointers are in bound and character at pointer l == character at pointer r
                res += 1 # increment count of result
                l -= 1 # move left pointer to left
                r += 1 # move right pointer to right
        
        return res