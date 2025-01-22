# Check if the two strings are anagrams

# Check lengths first

## Use dictionaries of character counts, check equality - O(m+n), O(m+n)
## Counter() does this automatically

## Sort strings, check equality - O(m log m + n log n), O(m+n)


def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
