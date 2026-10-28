class Node:
    def __init__(self, key, val): 
        self.key, self.val = key, val # key, value
        self.prev = self.next = None # previous and next pointers are None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity # capacity of the cache
        self.cache = {} # hashmap; maps key to node
        # left = LRU, right = MRU
        self.left, self.right = Node(0,0), Node(0,0) # left and right pointers at node 0
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node): # helper function to remove node from list
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev


    def insert(self, node): # helper function to add node to right most position (most recently used)
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev


    def get(self, key: int) -> int:
        if key in self.cache: # if key present in hashmap, return it
            self.remove(self.cache[key]) # remove node from list
            self.insert(self.cache[key]) # insert the node back at right most position
            return self.cache[key].val
        return -1 # if not present, return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache: # if key present in hashmap, remove it
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value) # insert node into hashmap 
        self.insert(self.cache[key]) # insert node into linked list

        if len(self.cache) > self.cap: # current cache length exceeded
            # remove node from list, and delete lru from hashmap (cache)
            lru = self.left.next # fetch the lru node
            self.remove(lru) # remove from list
            del self.cache[lru.key] # delete from hashmap (cache)  
