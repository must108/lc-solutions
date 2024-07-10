class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ret = 0
        for l in logs:
            if l == '../':
                ret -= 1
            elif l == './':
                continue
            else:
                ret += 1
            
            if ret < 0:
                ret = 0
        
        return ret