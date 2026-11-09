class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures) # days to wait for each day; 0 = no warmer day found
        stack = [] # indexes of days still waiting for a warmer day (temps decreasing from bottom to top)

        for i in range(len(temperatures)): # i - current day
            while stack and (temperatures[i] - temperatures[stack[-1]] > 0): # today is warmer than the most recent waiting day
                j = stack.pop() # j - index of the day that just found its warmer day, i - current index
                result[j] = i-j # days day j waited = difference of indexes, not temperatures
            stack.append(i) # current day now waits for its own warmer day
        return result # days left on the stack keep 0


#                 0  1  2  3  4  5  6
# temperatures = [30,38,30,36,35,40,28]
# result = [0 0 0 0 0 0 0]
# stack = []
# i=0, stack and (temperatures[i] - temperatures[stack[-1]] > 0): no, stack=[0]
# i=1, [0] and (38-30 > 0):yes, j=0, result[0]=1-0=1, result=[1 0 0 0 0 0 0], stack=[1]
# i=2, [1] and (30-38 > 0):no, stack = [1 2]
# i=3, [1 2] and (36-30 > 0):yes, j=2, result[2]=3-2=1, result=[1 0 1 0 0 0 0], stack=[1]
#      [1] and (36-38 > 0):no, stack=[1 3]
# i=4, [1 3] and (35-36 > 0):no, stack=[1 3 4]
# i=5, [1 3 4] and (40-35 > 0):yes, j=4, result[4]=5-4=1, result=[1 0 1 0 1 0 0], stack=[1 3]
#      [1 3] and (40-36 > 0):yes, j=3, result[3]=5-3=2, result=[1 0 1 2 1 0 0], stack=[1]
#      [1] and (40-38 > 0):yes, j=1, result[1]=5-1=4, result=[1 4 1 2 1 0 0], stack=[]
#      [] and :no, stack=[5]
# i=6, [5] and (28-40 > 0):no, stack=[5 6]
# return result [1 4 1 2 1 0 0]