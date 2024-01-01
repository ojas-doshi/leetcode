class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        count = 0
        char_count = defaultdict(int)
        for c in chars:
            char_count[c] = char_count[c] + 1
        
        for word in words:
            word_count = defaultdict(int)
            for c in word:
                word_count[c] = word_count[c] + 1
            
            result = True
            for c,freq in word_count.items():
                if char_count[c] < freq:
                    result = False
                    break
            if result:
                count += len(word)
        return count
        