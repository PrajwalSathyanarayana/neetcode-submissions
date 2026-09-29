# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = [] # result list
        q = collections.deque() # queue to keep track of elements

        q.append(root)  # insert root into queue
        while q:    # while q is not empty
            qLen = len(q)   # calculate the length of the current queue
            level = []  # sub list to add the node value by level
            for i in range(qLen):
                node = q.popleft()  # pop the first element added to queue
                if node: # if node is not empty
                    level.append(node.val) # insert node into level sub list
                    q.append(node.left) # insert the left child node
                    q.append(node.right)    # insert the right child node
            if level:
                result.append(level)
        return result            
            