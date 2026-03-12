# Time complexity: O(n)
# Space commplexity: O(1)


def container_with_most_water(height):

    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        water = (right - left) * min(height[left], height[right])
        max_water = max(max_water, water)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water

if __name__ == "__main__":
    assert container_with_most_water([4, 6, 8, 10, 12]) == 18