# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = [] # result array
        q = collections.deque([root]) # queue initialized with root

        while q: # while q is not empty
            rightSide = None # rightSide node is initialized to none
            qLen = len(q) # length of queue

            for i in range(qLen): # iterate through the queue
                node = q.popleft() # pop the left node from the queue
                if node: # if node is not null
                    rightSide = node # current node is rightSide
                    q.append(node.left) # append left child of current node to queue
                    q.append(node.right) # append right child of current node to queue
            if rightSide: # if rightSide is not null  
                res.append(rightSide.val) # append the value of rightSide to result               
        return res # return result