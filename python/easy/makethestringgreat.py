class Solution:
    def makeGood(self, s: str) -> str:
        sk = []

        for c in s:
            if sk and sk[-1] == c.swapcase():
                sk.pop()
            else:
                sk.append(c)

        return "".join(sk)