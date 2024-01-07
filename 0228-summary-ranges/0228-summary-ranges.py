class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ranges = []
        start = end = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                ranges.append(str(start) if start == end else f"{start}->{end}")
                start = end = nums[i]

        ranges.append(str(start) if start == end else f"{start}->{end}")
        return ranges