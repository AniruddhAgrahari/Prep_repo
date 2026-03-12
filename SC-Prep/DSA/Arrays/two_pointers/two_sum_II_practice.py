

def two_sum_II(nums, target):

    left = 0
    right = len(nums) - 1

    while left < right:
        s = nums[left] + nums[right]
        if s == target:
           return [left+1, right+1]
        elif s > target:
            right -= 1
        elif s < target:
            left += 1

if __name__ == "__main__":
    assert two_sum_II([1, 2, 4, 8], 3) == [1, 2]
    assert two_sum_II([1, 3, 5, 7, 9], 16) == [4, 5]
    assert two_sum_II([3, 4, 7, 6, 10], 9) == [1, 4]