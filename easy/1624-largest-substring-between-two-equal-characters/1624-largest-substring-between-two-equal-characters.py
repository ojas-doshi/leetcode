class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = -1
        char_index = {}

        for i, char in enumerate(s):
            if char not in char_index:
                char_index[char] = i
            else:
                max_length = max(max_length, i - char_index[char] - 1)

        return max_length