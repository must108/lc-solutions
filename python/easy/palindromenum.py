class Solution:
    def isPalindrome(self, x: int) -> bool:
        str1 = str(x)
        str2 = str(x)
        return str1 == str2[::-1]