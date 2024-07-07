class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        t = numBottles
        res = numBottles

        while t > 0:
            rem = t % numExchange
            t = int(t / numExchange)
            if t:
                res += t
                t += rem

        return res