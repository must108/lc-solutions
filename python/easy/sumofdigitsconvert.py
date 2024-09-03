class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ""

        for c in s:
            val = ord(c) - ord('a') + 1
            num += str(val)

        while k > 0:
            total = 0
            for c in num:
                total += int(c)
            num = str(total)

            k -= 1

        return int(num)