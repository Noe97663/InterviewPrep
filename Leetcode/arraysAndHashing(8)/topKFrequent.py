# given an array of nums and int k,
# return the k most frequent elements

## Brute force - make count dictionary, then sort key value pairs -O(n. log n), O(n)
## Heap method - O(k. log n) [ number of elements . pop from heap], O(n)
## Optimal- Count elements, put into frequency array, iterate - O(n), O(n)


def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)

    # the index in freq corresponds to how many times an element appeared
    freq = [[] for i in range(len(nums) + 1)]
    for num, cnt in count.items():
        freq[cnt].append(num)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res
