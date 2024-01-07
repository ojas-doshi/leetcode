class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search_helper(self, word, node):
        for i in range(len(word)):
            char = word[i]
            if char == '.':
                for child in node.children.values():
                    if self.search_helper(word[i+1:], child):
                        return True
                return False
            elif char in node.children:
                node = node.children[char]
            else:
                return False
        return node.is_end_of_word

    def search(self, word):
        return self.search_helper(word, self.root)
