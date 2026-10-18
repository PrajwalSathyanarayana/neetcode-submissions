"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        OldToNew = {} # hashmap
        
        def dfs(node): # recursive DFS
            if node in OldToNew:    # if node is in hashmap, then then node is already cloned i.e., copy of original node exisits in the hashmap
                return OldToNew[node] # return the node
            copy = Node(node.val) # create a copy of the node; Node - constructor, node.val - value of the node
            OldToNew[node] = copy   # map the old node to the copied node in the hashmap

            for nei in node.neighbors: # iterate through every single neighbor
                copy.neighbors.append(dfs(nei)) # append the returned copy of neighbor the dfs was ran on and ended up creating; take the copy and its list of neighbors, and append the return statement from the dfs call.
            return copy # return the copy

        return dfs(node) if node else None  # pass the original node to dfs(), return None if original node is null/empty
        