class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        def count_vowels(string):
            vowels = set("aeiouAEIOU")
            count = 0
            for char in string:
                if char in vowels:
                    count += 1
            return count

        n = len(s)
        mid = n // 2

        a = s[:mid]
        b = s[mid:]

        count_a = count_vowels(a)
        count_b = count_vowels(b)

        return count_a == count_b