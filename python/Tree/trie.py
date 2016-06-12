class Node():
    
    def __init__(self,):
        self.child = {}
        self.end_of_word = False    
    
    def __str__(self):
        return "%s --> end_of_word : %s" % (self.child, self.end_of_word)
    
class Trie():
    
    def __init__(self):
        self.root = Node()
        
    def insert (self, word):
        current_node = self.root
        for char in word:
            if not current_node.child.get(char):
                node = Node()
                current_node.child[char] = node
                
            current_node = current_node.child.get(char)
        current_node.end_of_word = True
        return
        
    def search(self, word):
        current_node = self.root
        for char in word:
            if current_node.child.get(char):
                current_node = current_node.child.get(char)
            else:
                return False
        return current_node.end_of_word
    
    def prefix_search(self, word):
        current_node = self.root
        for char in word:
            if current_node.child.get(char):
                current_node = current_node.child.get(char)
            else:
                return False
        return True

    """
    TODO : implement delete
    """
    def delete(self, word):
        pass

if __name__ == "__main__":
    trie = Trie()
    trie.insert("abc")
    trie.insert("abcd")
    trie.insert("xyyz")
    print trie.search("abc")
    print trie.prefix_search("xy")
    print trie.prefix_search("xyz")
                
