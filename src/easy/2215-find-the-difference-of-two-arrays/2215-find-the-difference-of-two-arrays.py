class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        answer = [
            list(set1 - set2),  # Elements in nums1 but not in nums2
            list(set2 - set1)   # Elements in nums2 but not in nums1
        ]

        return answer