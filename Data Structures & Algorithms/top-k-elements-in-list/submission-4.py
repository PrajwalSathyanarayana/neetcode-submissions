class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # hashmap ro keep track of frequency values
        freq = [[] for i in range(len(nums) + 1)] # frequency array the size of nums + 1 to store list of values

        for n in nums: # loop through nums
            count[n] = 1 + count.get(n, 0) # increment the count of current number, if not present, default 0

        for n,c in count.items(): # loop through freq
            freq[c].append(n) # append current value to freq

        result = [] # result list to store the top k elements

        for i in range(len(freq)-1, 0 , -1): # loop through freq in descending order
            for n in freq[i]: # loop through each value
                result.append(n) # append the value to result 
                if len(result) == k: # when length of result is same as k
                    return result # return result
