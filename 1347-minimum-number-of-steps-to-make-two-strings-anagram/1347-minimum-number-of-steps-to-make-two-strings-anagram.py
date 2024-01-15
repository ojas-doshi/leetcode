class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # Check if lengths of both strings are equal
        if len(s) != len(t):
            return -1  # Return an error code or handle the error appropriately

        # Initialize an array to store the count of each character
        count_s = [0] * 26  # Assuming lowercase English letters only

        # Count the occurrences of each character in string s
        for char in s:
            count_s[ord(char) - ord('a')] += 1

        # Iterate through string t and decrement the count for each character
        # If a character is not present in s, increment the steps
        steps = 0
        for char in t:
            index = ord(char) - ord('a')
            if count_s[index] > 0:
                count_s[index] -= 1
            else:
                steps += 1

        return steps