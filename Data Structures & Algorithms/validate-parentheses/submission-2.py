class Solution:
    def isValid(self, s: str) -> bool:
        pairs = { # defined pairs of parentheses, {close: open}
            '}':'{',
            ']':'[',
            ')':'(',
        }
        stack = [] # stack to keep track of parentheses

        for c in s: # iterate through input string
            if c in pairs: # check if the current character is a closing parenthese i.e., its present in hashmap
                if stack and stack[-1] == pairs[c]: # make sure stack is not empty and value at top of the stack is matching open parentheses
                    stack.pop() # parentheses match => pop from stack
                else: # if they don't match or stack is empty
                    return False # return False
            else: # if encounter an open parentheses
                stack.append(c)
        
        return True if not stack else False # return true if stack is empty

