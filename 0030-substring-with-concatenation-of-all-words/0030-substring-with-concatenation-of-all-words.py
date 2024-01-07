class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        wordCount = Counter(words)
        wordLen = len(words[0])
        totalLen = len(words) * wordLen
        result = []

        for i in range(len(s) - totalLen + 1):
            wordSeen = {}
            for j in range(0, totalLen, wordLen):
                word = s[i + j:i + j + wordLen]
                if word in wordCount:
                    wordSeen[word] = wordSeen.get(word, 0) + 1
                    if wordSeen[word] > wordCount[word]:
                        break
                else:
                    break
            if wordSeen == wordCount:
                result.append(i)

        return result