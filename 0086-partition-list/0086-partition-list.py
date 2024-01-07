# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head = ListNode(0)
        greater_head = ListNode(0)
        less_ptr = less_head
        greater_ptr = greater_head

        while head:
            if head.val < x:
                less_ptr.next = head
                less_ptr = less_ptr.next
            else:
                greater_ptr.next = head
                greater_ptr = greater_ptr.next
            head = head.next

        greater_ptr.next = None  # Set end of greater list to None to avoid cycle

        less_ptr.next = greater_head.next  # Connect the two lists

        return less_head.next  # Return the merged list
