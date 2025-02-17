# list all the elements of a matrix in spiral order

## Iteration - iterate in the correct order with 4 bounds
##           - O(m. n), O(1)


# can shorten the code with a direction matrix [ [0,1], [1,0], .. , .. ]
def spiralOrder(matrix: [[int]]) -> [int]:
    res = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)

    while left < right and top < bottom:
        # go right
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1
        # go down
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right -= 1
        # check if anything left
        if not (left < right and top < bottom):
            break
        # go left
        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])
        bottom -= 1
        # go up
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        left += 1

    return res
