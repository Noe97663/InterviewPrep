# Need to store the most water

## Brute force - nested loop - O(n^2), O(1)
## Optimal - Two pointer solution - O(n), O(1)
##           You are always limited by the shortest bar


def maxArea(heights: list[int]) -> int:
    area_max = 0
    l, r = 0, len(heights) - 1
    while l < r:
        area = (r - l) * min(heights[l], heights[r])
        area_max = max(area, area_max)
        if heights[l] > heights[r]:
            r -= 1
        else:
            l += 1
    return area_max
