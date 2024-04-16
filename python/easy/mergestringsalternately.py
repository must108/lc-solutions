class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        str1 = ""
        count = 0

        while count < len(word1) or count < len(word2):
            if count < len(word1):
                str1 += word1[count]

            if count < len(word2):
                str1 += word2[count]

            count += 1

        return str1
