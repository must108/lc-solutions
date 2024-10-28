class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        n = len(logs)
        h = {}

        h[logs[0][1]] = logs[0][0]
        for i in range(1, n):
            t = logs[i][1]-logs[i-1][1]
            if t not in h:
                h[t] = logs[i][0]
            else:
                h[t] = logs[i][0] if h[t] > logs[i][0] else h[t]

        return h[max(h)]
            