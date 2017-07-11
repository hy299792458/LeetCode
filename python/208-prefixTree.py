class Trie(object):

    def __init__(self):
        self.tree = [dict()]
        
        

    def insert(self, word):
        word += '$'
        pos = 0
        for char in word:
            if char not in self.tree[pos]:
                self.tree[pos][char] = len(self.tree)
                self.tree.append(dict())
            pos = self.tree[pos][char]
                

    def search(self, word):
        word += '$'
        return self.startsWith(word)
        
    def startsWith(self, prefix):
        pos = 0
        for char in prefix:
            if char not in self.tree[pos]:
                return False
            pos = self.tree[pos][char]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
