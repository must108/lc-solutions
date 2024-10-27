class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        e = o = 0
        for num in position:
            if num % 2 == 0:
                e += 1
            elif num % 2 == 1:
                o += 1

        return min(e, o)