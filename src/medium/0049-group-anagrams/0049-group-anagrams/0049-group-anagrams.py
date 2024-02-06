class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
    
        for word in strs:
            # Sort the characters of the word to use as a key in the dictionary
            sorted_word = ''.join(sorted(word))
            # Add the word to the list of anagrams corresponding to the sorted_word key
            anagrams[sorted_word].append(word)

        return list(anagrams.values())