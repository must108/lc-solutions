class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()

        n = len(deck)
        res = [None] * n
        index = []

        for i in range(n):
            index.append(i)

        for card in deck:
            idx = index[0]
            index.pop(0)
            res[idx] = card
            if index:
                index.append(index[0])
                index.pop(0)

        return res