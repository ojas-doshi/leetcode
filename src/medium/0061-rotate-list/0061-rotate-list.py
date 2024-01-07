# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        # Calculate the length of the linked list
        length = 1
        old_tail = head
        while old_tail.next:
            old_tail = old_tail.next
            length += 1

        # Actual number of rotations required
        k %= length

        if k == 0:
            return head

        # Find the new tail by moving (length - k) steps from the head
        new_tail_position = length - k
        new_tail = head
        for i in range(1, new_tail_position):
            new_tail = new_tail.next

        # Set the new tail and break the list
        new_head = new_tail.next
        new_tail.next = None
        old_tail.next = head  # Connect the original tail to the original head

        return new_head