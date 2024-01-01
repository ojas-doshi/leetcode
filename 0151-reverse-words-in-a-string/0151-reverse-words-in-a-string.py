class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Split the string by spaces to get individual words
        words = s.split()

        # Reverse the list of words
        words.reverse()

        # Join the reversed words with a single space
        return ' '.join(words)
