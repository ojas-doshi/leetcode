class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        result = []
        window = deque()

        for i, num in enumerate(nums):
            # Remove indices that are outside the current window
            while window and window[0] < i - k + 1:
                window.popleft()

            # Remove indices of elements smaller than the current element
            while window and nums[window[-1]] < num:
                window.pop()

            window.append(i)

            # Add maximum element of current window to the result
            if i >= k - 1:
                result.append(nums[window[0]])

        return result