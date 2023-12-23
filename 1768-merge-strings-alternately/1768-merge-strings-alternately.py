class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        min_len = min(len(word1),len(word2))

        merged = ""
        for i in range(min_len):
            merged = merged + word1[i] + word2[i]

        return merged + word1[min_len:] + word2[min_len:]

        