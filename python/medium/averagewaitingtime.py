class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        avg = 0
        c = 0

        for cust in customers:
            c = max(cust[0], c) + cust[1]
            avg += c - cust[0]

        return avg / len(customers)