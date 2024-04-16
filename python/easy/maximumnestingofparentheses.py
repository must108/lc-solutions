class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maximum = 0
        n = len(s)

        for i in range(n):
            if(s[i] == '('):
                count += 1
                maximum = max(maximum, count)
            elif(s[i] == ')'):
                count -= 1
                maximum = max(maximum, count)

        return maximum