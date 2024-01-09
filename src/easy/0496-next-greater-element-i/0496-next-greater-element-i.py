class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        result = [-1] * len(nums1)
        for i, num in enumerate(nums1):
            if num in next_greater:
                result[i] = next_greater[num]

        return result