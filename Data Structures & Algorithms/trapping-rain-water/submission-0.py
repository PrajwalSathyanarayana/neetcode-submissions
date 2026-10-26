class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height: # if empty => return 0
            return 0
        
        l, r = 0, len(height)-1 # 2 pointers left and right
        leftMax, rightMax = height[l], height[r] # 2 pointers to keep track of max
        res = 0 # result

        while l<r: # while pointers in bound
            if leftMax < rightMax:
                l += 1  
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
            
        return res