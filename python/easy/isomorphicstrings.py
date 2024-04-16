class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1 = {}
        m2 = {}
        n = len(s)

        for i in range(n):
            if (m1.get(s[i]) and m1.get(s[i]) != t[i]) or (m2.get(t[i]) and m2.get(t[i]) != s[i]):
                return False

            m1[s[i]] = t[i]
            m2[t[i]] = s[i]

        return True