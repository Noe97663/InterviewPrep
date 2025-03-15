# add one to a number whose digits are made up by
# elements in an array

## bruh - go through arr, if 9 -> 0, keep going
##                        else +1 - O(n), O(n)





def plusOne(digits: [int]) -> [int]:
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    
    return [1] + digits

# recursion
def plusOne(digits: [int]) -> [int]:
    if not digits:
        return [1]

    if digits[-1] < 9:
        digits[-1] += 1
        return digits
    else:
        return plusOne(digits[:-1]) + [0]