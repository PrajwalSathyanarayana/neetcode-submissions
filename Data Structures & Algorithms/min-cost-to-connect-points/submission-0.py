class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points) # number of nodes
        adj = {i : [] for i in range(N)} # adjacency list {i : list of [cost,node]}

        # calculating the cost of edge using manhattan distance
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2) # Manhattan distance
                adj[i].append([dist,j]) # append the (distance, node) to adjacency list; undirected, hence both ways
                adj[j].append([dist,i]) # append the (distance, node) to adjacency list
        
        # PRIM's algorithm
        res = 0 # total cost
        visit = set() # hashset 
        minH = [[0,0]] # [cost, node]; min heap
        while len(visit)<N: # length of visited set < N
            cost, i = heapq.heappop(minH) # pop from min heap
            if i in visit: # if node is already visited, skip iteration
                continue 
            res += cost # add cost to result
            visit.add(i) # add node to visited set
            for neiCost, nei in adj[i]: # iterate through adjacency list
                if nei not in visit: # if node not in visited, push it to min heap
                    heapq.heappush(minH, [neiCost, nei])
        return res # return result