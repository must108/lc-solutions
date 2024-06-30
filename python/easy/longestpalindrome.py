class Solution:
    def longestPalindrome(self, s: str) -> int:
        h = {}
        r = 0
        o = False

        for st in s:
            h[st] = 1 + h.get(st, 0)

        for st in h:
            if h[st] % 2 == 0:
                r += h[st]
            else:
                r += h[st] - 1
                o = True

        if o:
            return r+1
        else:
            return r