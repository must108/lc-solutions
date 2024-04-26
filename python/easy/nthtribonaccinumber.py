class Solution:
    def tribonacci(self, n: int) -> int:
        m = {}

        def help(n):
            if n in m:
                return m[n]
            elif n == 0:
                return 0
            elif n == 1 or n == 2:
                return 1
            else:
                res = help(n-1) + help(n-2) + help(n-3)
                m[n] = res
                return res
            
        return help(n)