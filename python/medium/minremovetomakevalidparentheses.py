class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        sk = []
        n = len(s)
        arr = list(s)

        for i in range(n):
            if arr[i] == '(':
                sk.append(i)
            elif arr[i] == ')':
                if sk:
                    sk.pop()
                else:
                    arr[i] = '*'

        while sk:
            arr[sk[-1]] = '*'
            sk.pop()

        res = ""
        for c in arr:
            if c is not '*':
                res += c

        return res