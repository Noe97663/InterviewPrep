# given nxn matrix, rotate it 90 degrees

## Brute force - copy it into another matrix, reassign
##             - O(n^2), O(n^2)
## Manual - reassign elements manually using one variable
##        - O(n^2), O(1)
## Transpose - the movement is a reverse+transpose
##           - O(n^2), O(1)


# reverse + transpose
def rotate(matrix: [[int]]) -> None:
    # Reverse the matrix vertically
    matrix.reverse()

    # Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# manual
def rotate(matrix: [[int]]) -> None:
    l, r = 0, len(matrix) - 1
    while l < r:
        for i in range(r - l):
            top, bottom = l, r

            # save the topleft
            topLeft = matrix[top][l + i]

            # move bottom left into top left
            matrix[top][l + i] = matrix[bottom - i][l]

            # move bottom right into bottom left
            matrix[bottom - i][l] = matrix[bottom][r - i]

            # move top right into bottom right
            matrix[bottom][r - i] = matrix[top + i][r]

            # move top left into top right
            matrix[top + i][r] = topLeft
        r -= 1
        l += 1
