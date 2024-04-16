class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        size = len(flowerbed)
        for i in range(size):
            if flowerbed[i] == 0:
                if i == 0 or flowerbed[i - 1] == 0:
                    if i == size - 1 or flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        count += 1

        return count >= n