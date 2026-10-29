class Solution:
    def reorganizeString(self, s: str) -> str:
        
        count = Counter(s) # hashmap, count of each character 
        maxHeap = [[-cnt,char] for char,cnt in count.items()] # list of frequency, character
        heapq.heapify(maxHeap) # list to heap

        prev = None # previous character
        res = "" # result string

        while maxHeap or prev: # either of them is not empty, then execute the loop
            if prev and not maxHeap: # previous character still exists, but heap is empty
                return ""
            
            # most frequent character, except previous
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        
        return res