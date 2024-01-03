class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each element
        count = Counter(nums)

        # Create a list of buckets to store elements based on their frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        # Place elements in the corresponding bucket based on their frequency
        for num, freq in count.items():
            buckets[freq].append(num)

        # Collect the top k frequent elements
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            result.extend(buckets[i])
            if len(result) >= k:
                break

        return result[:k]