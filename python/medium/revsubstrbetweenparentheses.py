class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = []
        temp = ""

        for c in s:
            if c == '(':
                stk.append(temp)
                temp = ''
            elif c == ')':
                temp = temp[::-1]
                if stk:
                    temp = stk.pop() + temp
            else:
                temp = temp + c     

        return temp