# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        # Get lengths of both linked lists
        lenA, lenB = 0, 0
        currentA, currentB = headA, headB

        while currentA:
            lenA += 1
            currentA = currentA.next

        while currentB:
            lenB += 1
            currentB = currentB.next

        # Reset pointers to the heads
        currentA, currentB = headA, headB

        # Move the longer linked list's pointer to align lengths
        while lenA > lenB:
            currentA = currentA.next
            lenA -= 1

        while lenB > lenA:
            currentB = currentB.next
            lenB -= 1

        # Move both pointers until they intersect or reach the end
        while currentA != currentB:
            currentA = currentA.next
            currentB = currentB.next

            if currentA is None and currentB is None:
                return None  # No intersection found

        return currentA  # Intersection node found