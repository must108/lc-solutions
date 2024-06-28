class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        deg = [0] * n

        for e in roads:
            deg[e[0]] += 1
            deg[e[1]] += 1

        deg.sort()

        val = 1
        res = 0
        for num in deg:
            res += val * num
            val += 1
        return res