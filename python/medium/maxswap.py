class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 10:
            return num

        ls = list(str(num))
        n = len(ls)
        post = [0] * n

        post[n-1] = n-1
        for i in range(n-2, -1, -1):
            if ls[i] > ls[post[i+1]]:
                post[i] = i
            else:
                post[i] = post[i+1]

        for i in range(n):
            if ls[i] < ls[post[i]]:
                ls[i], ls[post[i]] = ls[post[i]], ls[i]
                return int("".join(ls))

        return num 
