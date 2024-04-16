class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ret = []
        checker = True
        n = len(candies)

        for i in range(n):
            for j in range(n):
                if candies[i] + extraCandies >= candies[j]:
                    checker = True
                else:
                    checker = False
                    break

            ret.append(checker)

        return ret