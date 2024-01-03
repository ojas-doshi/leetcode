# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Function to reverse a linked list
        def reverseLinkedList(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev

        # Function to find the middle of the linked list
        def findMiddle(node):
            slow = node
            fast = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        if not head or not head.next:
            return True

        # Find the middle of the linked list
        mid = findMiddle(head)

        # Reverse the second half of the linked list
        second_half = reverseLinkedList(mid)

        # Compare the first half and the reversed second half
        while second_half:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next

        return True