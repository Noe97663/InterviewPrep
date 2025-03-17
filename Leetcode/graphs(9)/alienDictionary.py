# given a dictionary of words, determine the order of the alphabet
# if the order is valid

## DFS - build an adjacency matrix of letters: letters that come after
##       use the matrix for DFS, making sure to detect cycles, at the end
##       of a DFS call, add the letter to a result string, return the
##       reversed string - O( n letters + V + E for dfs ), O( V + E )
## Topological sort - same runtime


def foreignDictionary(words: [str]) -> str:
    # build adjacency matrix
    adj = {c: set() for w in words for c in w}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        minLen = min(len(w1), len(w2))
        # invalid dictionary/ordering
        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
            return ""
        # find successor
        for j in range(minLen):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                break

    visited = {}
    res = []

    def dfs(char):
        if char in visited:
            return visited[char]

        visited[char] = True

        for neighChar in adj[char]:
            if dfs(neighChar):
                return True

        visited[char] = False
        # append to result after traversing dfs
        # i.e. adding leaf nodes first
        res.append(char)

    for char in adj:
        if dfs(char):
            return ""

    res.reverse()
    return "".join(res)
