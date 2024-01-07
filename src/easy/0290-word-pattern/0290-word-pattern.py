class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        pattern_map = {}
        word_map = {}

        for i in range(len(pattern)):
            if pattern[i] not in pattern_map:
                pattern_map[pattern[i]] = words[i]
            else:
                if pattern_map[pattern[i]] != words[i]:
                    return False

            if words[i] not in word_map:
                word_map[words[i]] = pattern[i]
            else:
                if word_map[words[i]] != pattern[i]:
                    return False

        return True