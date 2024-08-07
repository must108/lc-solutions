class Solution:
    def minimumPushes(self, word: str) -> int:
        b = [0] * 26
        ret = 0

        for l in word:
            b[ord(l) - 97] += 1
        b.sort(reverse=True)
    
        for i in range(26):
            if b:
                ret += (i//8 + 1) * b[i]
            else:
                break

        return ret