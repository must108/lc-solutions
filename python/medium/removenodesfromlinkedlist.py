class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = []
        temp = head

        temp = head
        while temp:
            while s and s[-1].val < temp.val:
                s.pop()
            s.append(temp)
            temp = temp.next
                
        nxt = None
        while s:
            temp = s.pop()
            temp.next = nxt
            nxt = temp

        return temp