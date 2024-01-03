# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currentNode = head
        while currentNode is not None and currentNode.next is not None:
            currentNode.val,currentNode.next.val = currentNode.next.val, currentNode.val
            currentNode = currentNode.next.next
        return head