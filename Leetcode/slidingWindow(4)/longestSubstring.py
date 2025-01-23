# Find the longest substring without duplicates

## Brute force - nested loop - O(n^2), O(1)
## Sliding window - classic - O(n), O(1)


def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0
    chars = set()
    l, r = 0, 1
    chars.add(s[0])
    max_len = 1
    while r < len(s):
        if s[r] in chars:
            while s[r] in chars:
                if s[l] in chars:
                    chars.remove(s[l])
                l += 1
        chars.add(s[r])
        if len(chars) > max_len:
            max_len = len(chars)
        r += 1
    return max_len
