# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None

        while temp is not None:
            front = temp.next   # 1. Save next node
            temp.next = prev    # 2. Reverse the link
            prev = temp         # 3. Step up prev node
            temp = front        # 4. Step up temp node

        return prev