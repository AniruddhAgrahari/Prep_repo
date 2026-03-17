# sliding window template
#  Initialize left = 0, window_sum = 0, max_sum = 0
# Expand: Move right pointer, add element to
# window_sum
# Shrink: once window size hits k, record answer,
# remove left element, move left
# Time: O(n) - each element enters and leaves window 
# at most once

def maximum_sub_array(nums, k):
    
    window_sum = 0

    for i in range(k):
        window_sum += nums[i]

    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i]
        window_sum -= nums[i-k]
        if max_sum < window_sum:
           max_sum = window_sum

    

    return max_sum


print(maximum_sub_array([2, 1, 5, 1, 3, 2], 3))
print(maximum_sub_array([1, 1, 1, 1], 2))
print(maximum_sub_array([5], 1))
print(maximum_sub_array([2, -1, -6, 4], 3))