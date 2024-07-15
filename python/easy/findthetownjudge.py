class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        h = {}

        if n > 1:
            for p, j in trust:
                if p not in h:
                    h[p] = [0, 0]
                if j not in h:
                    h[j] = [0, 0]

                h[p][0] += 1
                h[j][1] += 1

            for k in h:
                if h[k][0] == 0 and h[k][1] == (n-1):
                    return k

            return -1
        else:
            return n