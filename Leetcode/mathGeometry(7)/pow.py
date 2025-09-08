# power of x^n - pow(x,n)

# just loop 4Head - O(n), O(1)
# exponentiation with squaring - O(log n), O(1)

def myPow(x: float, n: int) -> float:
    if x == 0:
        return 0
    if n == 0:
        return 1
    
    res = 1
    power = abs(n)
    
    while power:
        if power & 1:
            res *= x
        x *= x
        power >>= 1
    
    return res if n >= 0 else 1 / res