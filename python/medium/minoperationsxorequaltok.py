class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        return (n & 1) + self.hammingWeight(n >> 1)

    def minOperations(self, nums: List[int], k: int) -> int:
        for i in nums:
            k = k ^ i
        return self.hammingWeight(k)