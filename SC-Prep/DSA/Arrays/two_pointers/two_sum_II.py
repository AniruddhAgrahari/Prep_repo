#Approach:
# left pointer at index 0, right pointer at last index


def two_sum_target_1(nums, target):

    left = 0
    right = len(nums) - 1
    


    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left+1, right+1]
        elif current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
    
            
if __name__ == "__main__":
    assert two_sum_target_1([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum_target_1([1, 4, 7, 9], 16) == [3, 4]
    assert two_sum_target_1([2, 4, 6, 8, 11], 10) == [1, 4]


