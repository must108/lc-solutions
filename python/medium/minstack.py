class MinStack:
    stk = []

    def __init__(self):
        self.stk = []    
    
    def push(self, val: int) -> None:
        self.stk.append([val])

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        mini = float("inf")
        for num in self.stk:
            if mini > num[0]:
                mini = num[0]
        return mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()