class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        add = 0
        n = len(chalk)

        for i in range(n):
            add += chalk[i]
            if add > k:
                break

        k = k % add
        for i in range(n):
            if k < chalk[i]:
                return i
            else:
                k -= chalk[i]