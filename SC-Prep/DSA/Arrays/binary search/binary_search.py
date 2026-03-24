# left + (right - left) // 2 gives the same 
# mathematical result but never adds two large numbers together, 
# so overflow is impossible.
# time complexity: O(log n)
# space complexity: O(1)

def binary_search(nums, target):

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

print(binary_search([2, 4, 6, 8, 10], 6))
print(binary_search([2, 10], 2))
print(binary_search([-1, 2, 4, 6, 8, 10], 10))

