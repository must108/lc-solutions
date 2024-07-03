class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        arr = ['']
        cnt = 0
        it = 0

        for i in range(len(s)):
            if s[i] is not ' ':
                arr[cnt] += s[i]
                it = 0
            else:
                if it:
                    continue
                else:
                    arr.append('')
                    cnt += 1
                    it = 1

        arr = arr[::-1]
        return " ".join(arr).strip()
