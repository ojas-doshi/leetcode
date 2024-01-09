class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]

        # Function to check if a word can be typed using letters from only one row
        def in_same_row(word):
            word_set = set(word.lower())
            for row in rows:
                if word_set.issubset(row):
                    return True
            return False

        # Filter words that can be typed using letters from only one row
        return [word for word in words if in_same_row(word)]