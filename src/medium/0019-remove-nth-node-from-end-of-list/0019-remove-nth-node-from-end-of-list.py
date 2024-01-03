# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        # Move the second pointer to the n+1 th node from the beginning
        for i in range(n + 1):
            second = second.next

        # Move first and second pointers simultaneously
        while second is not None:
            first = first.next
            second = second.next

        # Remove the nth node from the end
        first.next = first.next.next

        return dummy.next