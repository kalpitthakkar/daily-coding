class TrieNode(object):

    def __init__(self,
                 LEN_CHARACTER_SET=26):
        
        self.children = [None] * LEN_CHARACTER_SET
        # True is the word ends here in the tree
        self.isEnd = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def _charToIndex(self, ch):
        return ord(ch) - ord('a')

    def _indexToChar(self, idx):
        return chr(ord('a') + idx)

    def insert(self, key):

        head = self.root
        length = len(key)

        for level in range(length):
            index = self._charToIndex(key[level])

            if head.children[index] is None:
                head.children[index] = TrieNode()
            head = head.children[index]

        head.isEnd = True

    def search(self, key):

        head = self.root
        length = len(key)

        for level in range(length):
            index = self._charToIndex(key[level])

            if head.children[index] is None:
                return "No word matches the given prefix"

            head = head.children[index]

        def traverse(head, string, matches=[]):
            if head.isEnd:
                matches.append(string)

            for idx in range(len(head.children)):
                if head.children[idx] is not None:
                    traverse(head.children[idx], string + self._indexToChar(idx), matches)

        matches = []
        traverse(head, key, matches)
        return matches

 
class Problem11(object):

    def __init__(self,
                 name):
        self.name = name
        self.trie = Trie()

    def insert(self, key):
        self.trie.insert(key)

    def search(self, key):
        return self.trie.search(key)
    
    def __repr__(self):
        return "Problem #11 [Medium]: " + self.name + "\nThis problem was asked by Twitter"

if __name__ == '__main__':
    p = Problem11('Given a query string, return all strings that contain it as prefix')
    print(p)

    strings = input("Enter the list of strings to use for queries (comma separated): ")
    strlist = [x for x in strings.split(',')]
    x = input("Enter query string: ")

    for s in strlist:
        p.insert(s)

    autocomplete = getattr(p, 'search')

    print("Strings that can be suggested in autocomplete: {}".format(autocomplete(x)))
