# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0 # variable to keep track of the number of elements visited
        stack = [] # stack to append elements visited
        cur = root # current value of the elements

        while cur or stack: # while current element is not null and stack is not empty
            
            while cur: # while current element is not null
                stack.append(cur) # append current value to stack so that we have to visit it back
                cur = cur.left
            
            cur = stack.pop() # pop the visited element from the stack
            
            n += 1  # increment the value of n (no. of element visited)
            if n == k: # if n is kth smallest element
                return cur.val    # return the value
            
            cur = cur.right