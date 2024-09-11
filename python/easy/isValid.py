class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        n = len(s)
        pairs = { '(':')', '{':'}', '[':']' }

        if n % 2 == 1:
            return False

        for c in s:
            if c in pairs:
                stk.append(c)
            else:
                if not stk:
                    return False
                else:
                    a = stk.pop()
                    if c != pairs[a]:
                        return False

        if stk:
            return False

        return True