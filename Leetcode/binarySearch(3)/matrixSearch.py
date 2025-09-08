# find a target in a sorted matrix - its just a sorted array tbh

# brute force - O(m. n), O(1)
# binary search - O(log(m. n)), O(1)


def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    ROWS, COLS = len(matrix), len(matrix[0])

    l, r = 0, ROWS * COLS - 1
    while l <= r:
        m = l + (r - l) // 2
        row, col = m // COLS, m % COLS
        if target > matrix[row][col]:
            l = m + 1
        elif target < matrix[row][col]:
            r = m - 1
        else:
            return True
    return False
