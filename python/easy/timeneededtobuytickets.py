class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        n = len(tickets)
        pos = tickets[k]
        seconds = 0
        while count < pos:
            for i in range(n):
                if tickets[i] > 0 and tickets[k] is not 0:
                    tickets[i] -= 1
                    seconds += 1
                elif tickets[k] == 0:
                    break

            count += 1

        return seconds