class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        char_count = Counter(''.join(words))
    
        for count in char_count.values():
            if count % len(words) != 0:
                return False

        return True
