# Group anagrams together into a 2D list - n strings of avg size m

## Brute force - sort all strings, group - O( n. m log m), O(m)
## Hashmap - (key,value) - (tuple of letter counts, words)
##          the values of the final hashmap will be the groups
##          O(n.m), O(n.m)

from collections import defaultdict


def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for s in strs:
        key = [0] * 26
        for c in s:
            idx = ord(c) - ord("a")
            key[idx] += 1
        groups[tuple(key)].append(s)
    return groups.values()
