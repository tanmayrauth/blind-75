"""
Datastructure used here to store the trie is Dict of dict. 
And while storing the data we need to use setdefault func of dict. While making a check you will have 2 options search and match for which you need to use False and True respectively for prefix value.

"""

class Trie:

    def __init__(self):
        self.T = {}
        
    def insert(self, word):
        node = self.T
        for c in word:
            node = node.setdefault(c, {})
        node['$'] = None
    
    def match(self, seq, prefix):
        node = self.T
        for c in seq:
            if c not in node:
                return False
            node = node[c]
        return prefix or ('$' in node)
    
    def search(self, word):
        return self.match(word, False)

    def startsWith(self, prefix):
        return self.match(prefix, True)
        