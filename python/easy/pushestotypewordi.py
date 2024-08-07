class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = 1
        h = {}
        for l in word:
            if cnt <= 8:
                h[l] = 1
            elif cnt <= 16:
                h[l] = 2
            elif cnt <= 24:
                h[l] = 3
            else:
                h[l] = 4

            cnt += 1

        return sum(h.values())