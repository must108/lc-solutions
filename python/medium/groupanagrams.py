class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        r = []

        for s in strs:
            t = ''.join(sorted(s))
            if t in h:
                h[t].append(s)
            else:
                h[t] = [s]

        [r.append(h[s]) for s in h]

        return r