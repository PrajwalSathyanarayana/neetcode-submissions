class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0 # result count

        def countPali(s, l, r):
            res = 0
            while ((l>=0) and (r<len(s)) and (s[l] == s[r])): # check if the pointers are in bound and character at pointer l == character at pointer r
                res += 1 # increment count of result
                l -= 1 # move left pointer to left
                r += 1 # move right pointer to right
        
            return res

        for i in range(len(s)): # iterate through every single character in string s
            res += countPali(s, i, i) # odd number length string
            res += countPali(s, i, i+1) # even number length string
        return res



