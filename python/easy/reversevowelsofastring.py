class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r, vow = 0, len(s) - 1, "aeiouAEIOU"
        s = list(s)

        while (l < r):
            while (l < r and s[l] not in vow):
                l += 1
            while (r > l and s[r] not in vow):
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return "".join(s)