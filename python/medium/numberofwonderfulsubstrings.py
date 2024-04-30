class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = defaultdict(int)
        count[0] = 1
        res = 0
        bitmsk = 0

        for char in word:
            idx = ord(char) - ord('a')
            bitmsk ^= 1 << idx
            res += count[bitmsk]
            for i in range(10):
                res += count[bitmsk ^ (1 << i)]
            count[bitmsk] += 1
        return res