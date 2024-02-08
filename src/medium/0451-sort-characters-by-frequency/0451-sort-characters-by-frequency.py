class Solution:
    def frequencySort(self, s: str) -> str:
        # Create a dictionary to store character frequencies
        freq_map = {}

        # Count frequencies of characters
        for char in s:
            freq_map[char] = freq_map.get(char, 0) + 1

        # Sort characters based on their frequencies in decreasing order
        sorted_chars = sorted(freq_map.keys(), key=lambda x: freq_map[x], reverse=True)

        # Generate the sorted string
        sorted_str = ''.join([char * freq_map[char] for char in sorted_chars])

        return sorted_str