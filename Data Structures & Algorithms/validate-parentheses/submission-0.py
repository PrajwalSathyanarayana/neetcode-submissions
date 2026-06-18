class Solution:
    def isValid(self, s: str) -> bool:
        s1 = [] # stack
        d = {
            '(':')',
            '[':']',
            '{':'}',
        }
        for i in s:
            if i in d:
                s1.append(i)
            else:
                if not s1:
                    return False
                else:
                    top = s1.pop()
                    if d[top] != i:
                        return False
        if not s1:
            return True
        else:
            return False