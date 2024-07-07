class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        return (k%(n-1)) if k//(n-1)%2==0 else n-(k%(n-1))-1