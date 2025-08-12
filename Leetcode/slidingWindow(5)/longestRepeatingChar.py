# given a string and an int k
# find the longest sequence of the same character possible
# if you can replace at most k characters

## Brute force - O(26. n), O(26) (check for 26 characters)
## Sliding window - O(n), O(1)


def characterReplacement(s: str, k: int) -> int:
    # helps to keep track of most common char (MCC) in window
    counts = {}
    res = 0
    l, r = 0, 0
    # checking every possible endpoint
    while r < len(s):
        counts[s[r]] = 1 + counts.get(s[r], 0)
        # while cannot cover non-MCC with k replacements
        while (r - l + 1) - max(counts.values()) > k:
            # make window smaller,
            # cause if [..|..|..] does not work,
            # [.|....|.] definitely wont
            counts[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
        r += 1
    return res
