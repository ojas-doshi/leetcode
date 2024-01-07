class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # Create a dictionary to count the occurrences of characters in magazine
        char_count = {}
        for char in magazine:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        # Iterate through the characters in ransomNote
        for char in ransomNote:
            # If the character is not in the magazine or its count is zero, return False
            if char not in char_count or char_count[char] == 0:
                return False
            # Decrement the count of the character in the dictionary
            char_count[char] -= 1

        # If all characters in ransomNote can be constructed, return True
        return True