'''
In Brute Force DFS time complexity: O(k * m * n * 4^(m*n)) where k = len(words)
But we can remove the k if we store all the words into a TRIE.
You need to understand how it is different from a normal string search even. Here we need Trie because we need to search amongst multiple words. So it is beneficial to use Trie here.

In word Search I we had only one word to search. I would suggest to understand diff bettwen I and II
To simultaneously check for all the words which can be created using list of word we need to use prefix tree fromat which is nothing but Trie else we can run that logic bt that will be time consuming.

'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
    
class Solution:
    def findWords(self, board, words):
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        row = len(board); col = len(board[0])
        res = set()
        
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= row or c >= col or 
                board[r][c] not in node.children or board[r][c] == '#'):
                return
            
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.endOfWord:
                res.add(word)
                
            tmp = board[r][c]
            board[r][c] = '#'
            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)
            board[r][c] = tmp
            
        for r in range(row):
            for c in range(col):
                dfs(r, c, root, "")
        
        return res
    
# Time: O(m * n * 4^(m*n))
# Space: O(m*n + k)