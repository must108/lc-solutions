class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        size = len(s) - 1

        for i in range(size, -1, -1):
            if s[i] == ' ':
                size -= 1
            else:
                break

        for i in range(size, -1, -1):
            if s[i] != ' ':
                length += 1
            else:
                break

        return length