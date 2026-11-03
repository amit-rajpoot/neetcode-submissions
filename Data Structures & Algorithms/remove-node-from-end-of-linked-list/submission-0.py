# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:

        slow = head
        fast = head

        # Move fast n steps ahead
        for i in range(n):
            fast = fast.next

        # If fast is None, delete head
        if fast is None:
            return head.next

        # Move both pointers
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        # Delete node
        slow.next = slow.next.next

        return head