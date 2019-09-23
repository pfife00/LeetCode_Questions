# 724. Find Pivot Index
# Easy
#
#
# Given an array of integers nums, write a method that returns the "pivot" index
# of this array.
#
# We define the pivot index as the index where the sum of the numbers to the left
# of the index is equal to the sum of the numbers to the right of the index.
#
# If no such index exists, we should return -1. If there are multiple pivot
# indexes, you should return the left-most pivot index.
#
# Example 1:
#
# Input:
# nums = [1, 7, 3, 6, 5, 6]
# Output: 3
# Explanation:
# The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum
# of numbers to the right of index 3.
# Also, 3 is the first index where this occurs.
#
#
# Example 2:
#
# Input:
# nums = [1, 2, 3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.
#
#
# Note:
#
# The length of nums will be in the range [0, 10000].
# Each element nums[i] will be an integer in the range [-1000, 1000].
#
# LOGIC
# 1) The sum left of the index (left_sum) is related to the sum right of the index
# by the relationship: Array_sum - left_sum - curr_val
#
# 2) So if left_sum equals Array_sum - left_sum - curr_val, then that index is the
# pivot
#
# 3) left_sum is tracked by summing val as iterate through array
#
#

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #find total sum of array
        nums_sum = sum(nums)
        left_sum = 0

        #i is index, curr_val is current value at index i
        for i, curr_val in enumerate(nums):
            if(left_sum == nums_sum - left_sum - curr_val):
                return i
            else:
                left_sum += curr_val
        return -1
