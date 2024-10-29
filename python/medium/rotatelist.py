# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        temp = head

        n = 1
        while temp.next:
            print(temp.val)
            temp = temp.next
            n += 1

        temp.next = head

        for _ in range(n-k % n):
            temp = temp.next
        
        for _ in range(n-k % n):
            head = head.next

        temp.next = None
        return head

        