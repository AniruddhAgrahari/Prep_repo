# Time complexity: O(n) - pass through n elements
# Space complexity: O(n) - dict stores at most n elements

def two_sum(nums, target):
    d = {}

    for i, num in enumerate(nums):

        complementt = target - num
        if complementt in d:
            return [d[complementt], i]
        else:
            d[num] = i


assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
assert two_sum([3, 3], 6) == [0, 1]