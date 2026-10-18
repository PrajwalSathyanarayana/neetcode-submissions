class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = {i:[] for i in range(numCourses)} # hashmap; map initial courses to empty list
        
        for crs, pre in prerequisites: # iterate through every prerequisite
            preMap[crs].append(pre) # add the prerequisite to the correspondding course

        visitSet = set() # Set to keep track of courses currently visiting

        def dfs(crs): # recursive DFS helper function
            if crs in visitSet: # base case 1, if course is currently in visited set, its a repeat => cyclic grapg never ending
                return False
            if preMap[crs] == []: # BC 2, if the pre-requisite of current course is empty list [], it means that current course is not dependent on any pre-requisite
                return True
            
            visitSet.add(crs) # add the currently visiting course to visitSet

            for pre in preMap[crs]: # for pre-requisite of a particular course in the hashmap
                if not dfs(pre): return False   # if dfs is false, return False

            visitSet.remove(crs)    # remove the currently visited course
            preMap[crs] = [] # empty list for that particular course in hashmap
            return True
        
        for crs in range(numCourses): # iterate through every course
            if not dfs(crs): return False # if dfs is false, return False
        
        return True # return True since dfs is Treu