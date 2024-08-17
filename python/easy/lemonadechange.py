class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        numFives = 0
        numTens = 0
        
        for bill in bills:
            if bill == 5:
                numFives += 1
            elif bill == 10:
                if numFives:
                    numFives -= 1
                    numTens += 1
                else:
                    return False
            elif bill == 20:
                if numFives and numTens:
                    numFives -= 1
                    numTens -= 1
                elif numFives and numFives >= 3:
                    numFives -= 3
                else:
                    return False

        return True
