class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        curr = temp
        total = 0
        head = head.next

        while head is not None:
            if head.val != 0:
                total += head.val
            else:
                curr.next = ListNode(total)
                curr = curr.next
                total = 0
            head = head.next

        return temp.next