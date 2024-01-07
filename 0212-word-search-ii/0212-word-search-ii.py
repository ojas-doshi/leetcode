
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node.word
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(node, i, j):
            if node.word:
                result.add(node.word)

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return

            char = board[i][j]
            if char not in node.children:
                return

            board[i][j] = '#'  # Mark visited cell

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                dfs(node.children[char], i + dx, j + dy)

            board[i][j] = char  # Backtrack

        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(trie.root, i, j)

        return list(result)
