class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in pairs:                       # closing bracket
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:                                  # opening bracket
                stack.append(ch)
        return not stack
