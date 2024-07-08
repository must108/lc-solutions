class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = list(range(1, n+1))
        t = 0

        while len(arr) > 1:
            r = (t+k-1)%len(arr)
            arr.pop(r)
            t = r

        return arr[0]