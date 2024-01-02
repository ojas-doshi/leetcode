# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        values = []
        current = head

        # Store values in an array
        while current:
            values.append(current.val)
            current = current.next

        # Initialize pointers
        left = 0
        right = len(values) - 1
        max_twin_sum = float('-inf')

        # Calculate twin sums
        while left < right:
            twin_sum = values[left] + values[right]
            max_twin_sum = max(max_twin_sum, twin_sum)
            left += 1
            right -= 1

        return max_twin_sum