class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = {}
        n = len(numbers)

        for i in range(n):
            get = target - numbers[i]
            if get in h and h[get] != i:
                return [h[get] + 1, i + 1]
            h[numbers[i]] = i

        return []