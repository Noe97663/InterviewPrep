#given a list of cars and their speeds, determine how many fleets will arrive at the destination

## Brute force - nested loop - O(n^2), O(1)
## Optimal - Stack (or counter) - O(n. log n), O(n)

def carFleet(target: int, position: [int], speed: [int]) -> int:
    pair = [(p, s) for p, s in zip(position, speed)]
    pair.sort(reverse=True)
    stack = []
    for p, s in pair:  # Reverse Sorted Order
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)