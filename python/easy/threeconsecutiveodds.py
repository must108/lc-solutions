class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        res = 0
        for num in arr:
            if num % 2 == 1:
                res += 1
            elif num % 2 == 0:
                res = 0

            if res == 3:
                return True

        return res >= 3

