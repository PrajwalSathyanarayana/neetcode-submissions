class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = "" # result string
        resLen = 0 # length of result

        for i in range(len(s)): # iterate through every character in string s
            # odd length
            l,r = i,i # 2 pointers l and r initialized to current character
            while l>=0 and r<len(s) and s[l]==s[r]: # check if the pointers are in bound and the 2 characters left and right of current character is equal or not
                if (r-l+1) > resLen: # check if the current length > result length
                    res = s[l: r+1] # update result
                    resLen = r-l+1
                l -= 1 # update left pointer to leftside
                r += 1 # update right pointer to rightside

            
            # even length
            l, r = i, i+1 # 2 pointers initialized to current character and next character
            while l>=0 and r<len(s) and s[l]==s[r]: # check if the pointers are in bound and the 2 characters left and right of current character is equal or not
                if (r-l+1) > resLen: # check if the current length > result length
                    res = s[l: r+1] # update result
                    resLen = r-l+1
                l -= 1 # update left pointer to leftside
                r += 1 # update right pointer to rightside
        return res