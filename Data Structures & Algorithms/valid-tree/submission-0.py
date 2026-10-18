class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: # base case 1; empty graph => return True
            return True
        
        visit = set() # set to keep track of visited nodes

        adj = {i:[] for i in range(n)} # a hashmap; for every node, create a pair {i:[]}

        for n1, n2 in edges: # iterate through each pair of edges
            # In a pair [0,1], 0->1 and 1->0 since both nodes point to each other
            adj[n1].append(n2) # for node1, append the connected edge node2
            adj[n2].append(n1) # for node2, append the connected edge node1

        def dfs(i, prev): # recursive DFS; i - current node; prev - previous node which led to current node
            
            if i in visit: # current node already visited => return false => cyclic graph
                return False
            
            visit.add(i) # add the current node to visit set

            for j in adj[i]: # iterate through every neighbor of i
                if j == prev: # if node j == previous node, then continue to avoid false positive; 0->1 and 1->0
                    continue
                if not dfs(j,i): # recursive call dfs(current node j, previous node i) and if dfs(j,i) is false, return false; if not False => if True => return False;
                    return False
            
            return True
        
        return dfs(0, -1) and n == len(visit) # starting node, previous node