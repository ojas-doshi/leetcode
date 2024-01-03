# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        slow = head
        fast = head

        # Check if there's a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  # Cycle detected
                # Move one pointer to the head and keep the other at meeting point
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow  # Return the start of the cycle

        return None  # No cycle found