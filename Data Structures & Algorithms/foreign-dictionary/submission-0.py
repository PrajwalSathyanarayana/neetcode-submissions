class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c : set() for w in words for c in w}
        # for every single character in list of words, map it to a set
        
        for i in range(len(words)-1):  # iterate through every word
            
            w1, w2 = words[i], words[i+1] # word at i, word at i+1
            minlen = min(len(w1), len(w2)) # minimum length of the 2
            
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]: # len(w1) > len(w2) and minimum length of the word is same; BC1
                return ""
            
            for j in range(minlen):
                if w1[j] != w2[j]: # characters differ
                    adj[w1[j]].add(w2[j]) # add w2[j] to adjacency list with w1 as key
                    break
        
        visit = {} # False - visited; True - in path
        res = []

        def dfs(c): # recursive dfs
            
            if c in visit: # if character is visited
                return visit[c] 
            
            visit[c] = True # set the character to as in path
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)

        for c in adj: # iterate through adjacency list
            if dfs(c): # start at any character
                return ""
        
        res.reverse() # reverse the result
        return "".join(res) # return the result
