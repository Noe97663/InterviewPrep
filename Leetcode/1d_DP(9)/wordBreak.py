# given a string, determine whether the string can be split into
# words that are given to you in a set

# n - length of input string
# m - no. of words in given set
# t - max len of word in set

## Brute force - make a set of words, loop through the string,
##               recurse when you find a possible word, see if you
##               can reach the end of the string - O( n. 2^n ),
##               O( m.t + n )
## DP - add memoization for top down
##      bottom up - start working from the back and solve the smallest
##      possible problems until you reach the front - O(n.m.t), O(n)



def wordBreak(s: str, wordDict: [str]) -> bool:
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    # start building a truth list from the back
    # [ ... , False, False , True, False, True ]
    for i in range(len(s) - 1, -1, -1):
        for w in wordDict:
            if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break
    return dp[0]