class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        result = []
        p_len = len(p)
        p_counter = Counter(p)
        s_counter = Counter(s[:p_len - 1])

        for i in range(p_len - 1, len(s)):
            s_counter[s[i]] += 1
            if s_counter == p_counter:
                result.append(i - p_len + 1)

            s_counter[s[i - p_len + 1]] -= 1
            if s_counter[s[i - p_len + 1]] == 0:
                del s_counter[s[i - p_len + 1]]

        return result