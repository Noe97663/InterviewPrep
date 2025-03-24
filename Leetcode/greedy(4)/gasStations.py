# given 
# gas arr - gas at station
# cost arr - cost to reach next station
# determine which station you need to start at to finish loop
# if possible, else -1

## brute force - O(n^2), O(1)
## two pointer - O(n), O(1)
## greedy - O(n), O(1)


def canCompleteCircuit(gas: [int], cost: [int]) -> int:
    # is a cycle possible?
    if sum(gas) < sum(cost):
        return -1

    total = 0
    res = 0
    for i in range(len(gas)):
        total += (gas[i] - cost[i])
        # reset the total if it becomes negative
        # reset res to next station since so far it didnt work
        if total < 0:
            total = 0
            res = i + 1
    
    return res

# two pointer
def canCompleteCircuit(gas: [int], cost: [int]) -> int:
    n = len(gas)
    start, end = n - 1, 0
    tank = gas[start] - cost[start]
    while start > end:
        # start was invalid, move it back
        if tank < 0:
            start -= 1
            tank += gas[start] - cost[start]
        # start was valid, move end forward
        else:
            tank += gas[end] - cost[end]
            end += 1
    return start if tank >= 0 else -1