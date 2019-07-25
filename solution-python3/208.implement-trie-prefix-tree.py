class TrieNode:
    def __init__(self):
        self.path = 0  # this node is shared by how many nodes
        self.end = 0  # how many words end with this node
        self.map = [None for i in range(26)]  # hash map to find node by path


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not word:
            return 
        
        node = self.root
        node.path += 1
        for c in word:
            index = ord(c) - ord('a')
            if not node.map[index]:
                node.map[index] = TrieNode()
            node = node.map[index]
            node.path += 1

        node.end += 1
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if not word:
            return False

        node = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not node.map[index]:
                return False
            node = node.map[index]
        return node.end != 0
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if not prefix:
            return False

        node = self.root
        for i, c in enumerate(prefix):
            index = ord(c) - ord('a')
            if not node.map[index]:
                return False
            node = node.map[index]
        return i == len(prefix) - 1 or any(node.map)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == '__main__':
    trie = Trie()
    words = ['app', 'apple', 'able']
    for word in words:
        trie.insert(word)
    assert trie.search('able') == True
    assert trie.search('appp') == False
    assert trie.startsWith('ap') == True

