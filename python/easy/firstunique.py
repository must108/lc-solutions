class Solution:
    def firstUniqChar(self, s: str) -> int:
        h = {}
        n = len(s)

        for c in s:
            if c in h:
                h[c] += 1
            else:
                h[c] = 1

        for i in range(n):
            if h[s[i]] == 1:
                return i

        return -1