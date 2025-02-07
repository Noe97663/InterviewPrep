# You are given an array of distinct integers nums and a target integer target.
# Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.
# Unlimited repeated selection allowed

## Either you select curr or you dont - recursively
## (OR) only recurse when it makes sense to
## O( 2^(t/m) ), O( 2^(t/m) ) - t is target, m is minimum value


def combinationSum(nums: [int], target: int) -> [[int]]:
    res = []

    def dfs(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return
        if i >= len(nums) or total > target:
            return
        # DO
        cur.append(nums[i])
        dfs(i, cur, total + nums[i])
        # DONT
        cur.pop()
        dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return res


# slight optimization - no unnecessary calls
def combinationSum(nums: [int], target: int) -> [[int]]:
    res = []
    nums.sort()

    def dfs(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return

        for j in range(i, len(nums)):
            if total + nums[j] > target:
                return
            cur.append(nums[j])
            dfs(j, cur, total + nums[j])
            cur.pop()

    dfs(0, [], 0)
    return res
