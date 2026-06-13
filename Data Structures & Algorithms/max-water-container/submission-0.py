class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        mw=0
        while l<r:
            cw = (r-l) * (min(heights[l], heights[r]))
            mw = max(mw, cw)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return mw
