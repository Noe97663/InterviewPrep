# Given a 2D matrix of X and O's , change surround O's to X's
# surrounded - X's in 4 directions

# BFS - DFS - O(m. n), O(m. n)
## DSU is a solution as well - O(m. n), O(m. n)


# Both are correct:

# Initially thought inside-out, find O's inside border, BFS out

# Better answer - outside in - find O's on border, mark safe
#                            - all other O's are captured