class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        h = {}
        ret = []
        n = len(names)

        for i in range(n):
            h[heights[i]] = names[i]

        h = dict(sorted(h.items()))
        
        for num in h:
            ret.insert(0, h[num])

        return ret