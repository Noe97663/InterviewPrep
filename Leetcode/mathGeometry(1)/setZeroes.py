# Given an m x n matrix of integers matrix,
# if an element is 0, set its entire row and column to 0's.

## Brute force - user a duplicate matrix full of 1's, mark zeroes
##               when you see them in the original - O(m. n), O(m. n)
## Improvement - mark row/col True, mark zeroes later - O(m. n), O(m+n)
## Optimal - mark row/col as zero in matrix itself BUT row/col overlap,
#            so mark all in matrix except rowZero which is one variable
#          - O(m. n), O(1)


def setZeroes(self, matrix: List[List[int]]) -> None:
    ROWS, COLS = len(matrix), len(matrix[0])
    rowZero = False

    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    rowZero = True

    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0

    if rowZero:
        for c in range(COLS):
            matrix[0][c] = 0
