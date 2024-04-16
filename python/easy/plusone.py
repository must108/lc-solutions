class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = [str(i) for i in digits]
        num = int(''.join(temp))
        num += 1
        ret = [int(x) for x in str(num)]
        return ret
