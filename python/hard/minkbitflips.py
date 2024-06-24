class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        q = deque()
        count = 0
        n = len(nums)

        for i in range(n):
            if q and q[0] + k <= i:
                q.popleft()

            if (nums[i] + len(q)) % 2 == 0:
                if i + k > n:
                    return -1
                q.append(i)
                count += 1

        return count