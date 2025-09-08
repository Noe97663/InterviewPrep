# A check is turning a number to the sum of its digits squares
# see if the checks will be cyclical or the number will become 1

# say there are log n such numbers before they loop

## set - use set to keep track of numbers already visited - O(log n), O(log n)
## fast,slow pointers - use a fast and slow pointer to do checks 2x and 1x,
##                      when the numbers match, see if they're 1 
##                    - O(log n), O(1)


def isHappy(self, n: int) -> bool:
    slow, fast = n, self.sumOfSquares(n)

    while slow != fast:
        fast = self.sumOfSquares(fast)
        fast = self.sumOfSquares(fast)
        slow = self.sumOfSquares(slow)
    return True if fast == 1 else False
    
def sumOfSquares(self, n: int) -> int:
    output = 0

    while n:
        digit = n % 10
        digit = digit ** 2
        output += digit
        n = n // 10
    return output