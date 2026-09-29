# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def Valid(left, node, right):
            if not node: # if node empty
                return True
            if not (left < node.val < right):
                return False
            return (Valid(left, node.left, node.val) and
            (Valid(node.val, node.right, right)))
        
        return (Valid(float('-inf'), root, float('inf')))