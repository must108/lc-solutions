class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        h = {}
        ret = []

        for let in arr:
            h[let] = 1 + h.get(let, 0)

        for let in h:
            if h[let] == 1:
                ret.append(let)

        return ret[k-1] if k-1 < len(ret) else ""
