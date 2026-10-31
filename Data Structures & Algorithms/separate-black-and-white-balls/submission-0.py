class Solution:
    def minimumSteps(self, s: str) -> int:
        l = res = 0
        for r in range(len(s)):
            if s[r]=='0':
                res += (r-l)
                l += 1
        return res

#      012345 
# s = "000111"
# l=0, res=0
# r=0, s[0]==0:yes, res=0+0=0, l=1
# r=1, s[1]==0:yes, res=0+0=0, l=2
# r=2, s[2]==0:yes, res=0+0=0, l=3
# r=3, s[3]==0:no, res=0, l=3
# r=4, s[4]==0:no, res=0, l=3
# r=5, s[1]==0:no, res=0, l=3
# return res=0 

#      0123 
# s = "1100"
# l=0, res=0
# r=0, s[0]==0:no, res=0, l=0
# r=1, s[1]==0:no, res=0, l=0
# r=2, s[2]==0:yes, res=0+2=2, l=1
# r=3, s[3]==0:yes, res=2+2=4, l=2
# return res=4