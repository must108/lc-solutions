class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None

        while(head != None):
            temp = head.next
            head.next = rev
            rev = head
            head = temp

        return rev