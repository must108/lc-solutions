class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        count = 1
        temp = head
        store = []

        while temp and temp.next and temp.next.next:
            lval = temp.val
            mval = temp.next.val
            rval = temp.next.next.val

            if (lval < mval > rval) or (lval > mval < rval):
                store.append(count)

            count += 1
            temp = temp.next

        if len(store) < 2:
            return [-1, -1]

        m = min(store[i+1]-store[i] for i in range(len(store)-1))
        l = store[-1] - store[0]
        return [m, l]