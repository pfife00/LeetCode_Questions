# 747. Largest Number At Least Twice of Others
# Easy
#
# In a given integer array nums, there is always exactly one largest element.
#
# Find whether the largest element in the array is at least twice as much as
# every other number in the array.
#
# If it is, return the index of the largest element, otherwise return -1.
#
# Example 1:
#
# Input: nums = [3, 6, 1, 0]
# Output: 1
# Explanation: 6 is the largest integer, and for every other number in the array x,
# 6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
#
#
# Example 2:
#
# Input: nums = [1, 2, 3, 4]
# Output: -1
# Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
#
#
# Note:
#
# nums will have a length in the range [1, 50].
# Every nums[i] will be an integer in the range [0, 99].
#
# LOGIC
# 1) find the max value of the array
# 2) enumerate through the array
# 3) if the current value = max value, then max value index = current index
# 4) else if the current value is greater than max value / 2, then return -1
# 5) after loop, return max_index

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_val = max(nums)
        for i, curr_val in enumerate(nums):
            if curr_val == max_val:
                max_index = i
            elif(curr_val > (max_val/2)):
                return -1

        return max_index
