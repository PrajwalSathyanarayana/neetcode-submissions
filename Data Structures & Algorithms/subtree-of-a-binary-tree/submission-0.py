# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: # subRoot is empty i.e., empty tree is a subtree of root
            return True
        if not root: # root is empty i.e., subRoot (having nodes) cannot be a subtree of root
            return False

        if self.isSameTree(root, subRoot): # compare both the trees using helper function and if same, return True
            return True
        
        return (self.isSubtree(root.left, subRoot) or # compare the subRoot to left subtree of root or to the right subtree of root 
        (self.isSubtree(root.right, subRoot)))

    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: # root is empty, and subRoot is empty
            return True
        
        if root and subRoot and root.val == subRoot.val: # root and subRoot are not empty and root.val is equal to subRoot.val
            return (self.isSameTree(root.left, subRoot.left) and
            self.isSameTree(root.right, subRoot.right))

        return False # atleast one of the tree is null/empty and other tree is not empty