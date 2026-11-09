class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures) # result  
        stack = [] # stack

        for i in range(len(temperatures)):
            while stack and (temperatures[i] - temperatures[stack[-1]] > 0):
                j = stack.pop() # j - index of the day that just found its warmer day, i - current index
                result[j] = i-j # 
            stack.append(i) # push the current day into stack
        return result