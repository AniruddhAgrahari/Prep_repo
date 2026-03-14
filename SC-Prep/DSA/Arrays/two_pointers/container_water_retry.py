#Approach:
# the left pointer is pointing at 0 and the right at len(array) - 1
# water contained = width(right - left) * min(array[left], array[right])
# move the pointer inwards whichever has smaller height

# Time complexity - O(n) - single pass with two pointers
# Space comlexity - O(1) - no extra data structures

def max_area(height: list[int]) -> int:

    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        water_contained = (right - left) * min(height[left], height[right])
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
        if max_water < water_contained:
            max_water = water_contained

    return max_water


assert max_area([2, 3, 5]) == 4
assert max_area([4, 6, 8,7]) == 12