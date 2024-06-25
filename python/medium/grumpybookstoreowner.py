class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)

        sat = sum(customers[i] for i in range(n) if grumpy[i] == 0)
        moresat = sum(customers[i] for i in range(minutes) if grumpy[i] == 1)
        exsat = moresat

        for i in range(minutes, n):
            if grumpy[i] == 1:
                moresat += customers[i]
            if grumpy[i - minutes] == 1:
                moresat -= customers[i - minutes]
            exsat = max(exsat, moresat)

        return sat + exsat