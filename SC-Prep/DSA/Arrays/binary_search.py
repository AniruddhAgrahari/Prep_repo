

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

