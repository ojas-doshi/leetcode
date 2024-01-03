class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # If mid element is greater than the rightmost element,
            # the minimum element must be in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # If mid element is less than or equal to the rightmost element,
            # the minimum element must be in the left half including the mid element
            else:
                right = mid

        return nums[left]