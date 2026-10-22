# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val] # global result initialized with root

        def dfs(root): # recursive DFS; return max path sum without the split
            if not root: # if root is not present => return 0
                return 0
            
            leftMax = dfs(root.left) # dfs on left child node
            rightMax = dfs(root.right) # dfs on right child node
            leftMax = max(0, leftMax) # avoid -ve value
            rightMax = max(0, rightMax)

            # compute max path sum WITH split
            res[0] = max(res[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]