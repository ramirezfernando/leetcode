class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word: # b a d
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True
    
    def search(self, word: str) -> bool:

        def dfs(j, child):
            curr = child
            for i in range(j,len(word)):
                w = word[i]
                if w == ".":
                    for child in curr.children.values():  # keys letters, values are TrieNode's
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if w not in curr.children:
                        return False
                    curr = curr.children[w]
            return curr.endOfWord
        
        return dfs(0, self.root)