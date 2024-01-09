class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)

        # Find the intersection by taking the minimum frequency for each common element
        intersection = []
        for num in count1.keys():
            if num in count2:
                intersection.extend([num] * min(count1[num], count2[num]))

        return intersection