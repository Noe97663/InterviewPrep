# Two strings s and t
# find smallest substring with all of t's chars in s

## Brute force - check all possible substrings - O(n^2), O(n)
## Sliding window - keep dicts of char counts in t and window,
##                  shrink window only when all counts satisfied
##                  - O(n), O(1)


def minWindow(s: str, t: str) -> str:
    res = ""
    res_len = len(s) + 1
    if len(s) < len(t):
        return ""
    # counts of required chars
    t_map = {}
    for char in t:
        t_map[char] = t_map.get(char, 0) + 1

    # important vars, it does not matter which char counts
    # are satisfied, only that all of them are or aren't
    need = len(t_map)
    have = 0
    # counts of chars in the window
    s_map = {}

    l = 0
    for r in range(0, len(s)):
        curr_char = s[r]
        curr_val = s_map.get(curr_char, 0) + 1
        s_map[curr_char] = curr_val
        # we have enough of curr character
        if curr_char in t_map and curr_val == t_map[curr_char]:
            have += 1
            while l <= r and need == have:
                if r - l + 1 < res_len:
                    new_sub = s[l : r + 1]
                    res = new_sub
                    res_len = r - l + 1
                start_char = s[l]
                start_val = s_map.get(start_char, 0) - 1
                s_map[start_char] = start_val
                if start_char in t_map and start_val < t_map[start_char]:
                    have -= 1
                l += 1
    return res
