# Time Complexity: O(log n)
# Space Complexity: O(1)
# Pattern: Binary Search
# Variant: minimum in rotated sorted array

def rotated_array_min(nums):
    start = 0
    end = len(nums) - 1

    while start < end:

        mid = (start + end) // 2

        if nums[mid] > nums[end]:
            start = mid + 1
        elif nums[mid] <= nums[end]:
            end = mid

    return nums[start]



print(rotated_array_min([3, 4, 5, 1, 2]))
print(rotated_array_min([4, 5, 1, 2, 3]))
print(rotated_array_min([1, 2, 3, 4, 5]))
print(rotated_array_min([2, 1]))