# Time Complexity: O(log n)
# Space Complexity: O(1)
# Pattern: Binary Search
# Variant: Search Insert Position

def search_insert_integer(nums, target):

    start = 0
    end = len(nums) - 1

    while start <= end:

        mid = (start + end) // 2

        if nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            return mid
    return start


print(search_insert_integer([1, 3, 5, 6], 2))
print(search_insert_integer([1, 3, 5, 6], 7))
print(search_insert_integer([1, 3, 5, 6], 0))
print(search_insert_integer([1, 3, 5, 6], 5))