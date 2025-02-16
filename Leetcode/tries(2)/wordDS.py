# store words, should be able to search and find them
# words can contain wildcard character like b.t matches but/bat

## Brute force - use an array, just append words, check all of them
##             - O(m*n), O(m*n)
## HashMap - use a hashmap + place to store wildcard words
## Trie - bruh - O(len of word), O(Trie nodes)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    # DFS is key for recursing into all possible paths when seeing .
    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)
