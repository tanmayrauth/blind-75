class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        
        node['$'] = True
                
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        
        def helper(w, node):
            for i, c in enumerate(w):
                if c in node:
                    node = node[c]
                else:
                    if c == '.':
                        for x in node:
                            if x != '$' and helper(w[i+1:], node[x]):
                                return True
                    return False
            return '$' in node
			
        return helper(word, self.trie)