class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        b = [[] for i in range(len(nums) + 1)]
        r = []

        for n in nums:
            h[n] = 1 + h.get(n, 0)

        for n, c in h.items():
            b[c].append(n)

        for i in range(len(b) - 1, 0, -1):
            for n in b[i]:
                r.append(n)
                if len(r) == k:
                    return r