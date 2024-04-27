class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        dp = [0] * len(ring)

        for k in reversed(range(len(key))):
            ndp = [float("inf")] * len(ring)
            for r in range(len(ring)):
                for i, c in enumerate(ring):
                    if c == key[k]:
                        min_dist = min(
                            abs(r - i),
                            len(ring) - abs(r - i)
                        )
                        ndp[r] = min(
                            ndp[r],
                            min_dist + 1 + dp[i]
                        )
            dp = ndp
        return dp[0]