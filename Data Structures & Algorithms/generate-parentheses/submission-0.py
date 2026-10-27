class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                result.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        
        backtrack(0,0)
        return result
# n = 2
# stack = [], result = []

# backtrack(0, 0)
#   0 < 2: yes  # openN < n
#   stack = ['(']
#   backtrack(1, 0):

#       1 < 2: yes  # openN < n
#       stack = ['(', '(']
#       backtrack(2, 0):

#           2 < 2: no  # openN < n

#           0 < 2: yes  # closedN < openN
#           stack = ['(', '(', ')']
#           backtrack(2, 1):

#               2 < 2: no  # openN < n

#               1 < 2: yes  # closedN < openN
#               stack = ['(', '(', ')', ')']
#               backtrack(2, 2):

#                   openN == closedN == n: yes
#                   result = ["(())"]
#                   return

#               # Back to backtrack(2, 1)
#               stack.pop()  # remove ')'
#               stack = ['(', '(', ')']
#               return

#           # Back to backtrack(2, 0)
#           stack.pop()  # remove ')'
#           stack = ['(', '(']
#           return

#       # Back to backtrack(1, 0)
#       stack.pop()  # remove '('
#       stack = ['(']

#       # Continue to the second if statement
#       0 < 1: yes  # closedN < openN
#       stack = ['(', ')']
#       backtrack(1, 1):

#           1 < 2: yes  # openN < n
#           stack = ['(', ')', '(']
#           backtrack(2, 1):

#               2 < 2: no  # openN < n

#               1 < 2: yes  # closedN < openN
#               stack = ['(', ')', '(', ')']
#               backtrack(2, 2):

#                   openN == closedN == n: yes
#                   result = ["(())", "()()"]
#                   return

#               # Back to backtrack(2, 1)
#               stack.pop()  # remove ')'
#               stack = ['(', ')', '(']
#               return

#           # Back to backtrack(1, 1)
#           stack.pop()  # remove '('
#           stack = ['(', ')']

#           # Continue to the second if statement
#           1 < 1: no  # closedN < openN

#           return

#       # Back to backtrack(1, 0)
#       stack.pop()  # remove ')'
#       stack = ['(']
#       return

#   # Back to backtrack(0, 0)
#   stack.pop()  # remove '('
#   stack = []

#   # Continue to the second if statement
#   0 < 0: no  # closedN < openN

#   return

# Final result:
# result = ["(())", "()()"]
# stack = []