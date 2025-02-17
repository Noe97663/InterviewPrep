# Find the longest palindrome substring from a string

## Brute force - loop for start, end, check palindrome
##             - O(n^3), O(1)
## Two pointer - loop for middle, check palindromes INSIDE OUT
##             - O(n^2), O(1)


def longestPalindrome(s: str) -> str:
    resIdx = 0
    resLen = 0
    # start in the middle
    for i in range(len(s)):
        # odd length
        l, r = i, i
        # go inside out
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                resIdx = l
                resLen = r - l + 1
            l -= 1
            r += 1

        # even length
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                resIdx = l
                resLen = r - l + 1
            l -= 1
            r += 1

    return s[resIdx : resIdx + resLen]
