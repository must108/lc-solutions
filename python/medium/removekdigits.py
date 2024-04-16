class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        sk = []

        for digit in num:
            while sk and sk[-1] > digit and k > 0:
                sk.pop()
                k -= 1
            
            sk.append(digit)

        while k > 0 and sk:
            sk.pop()
            k -= 1

        temp = ""
        n = len(sk)
        for i in range(n):
            temp += sk[-1]
            sk.pop()
            
        temp = temp[::-1]

        ret = ""
        found = 0
        m = len(temp)
        for i in range(m):
            if temp[i] is '0' and found is 0:
                continue
            else:
                ret += temp[i]
                found = 1

        if len(ret) is 0:
            ret += '0'

        return ret

