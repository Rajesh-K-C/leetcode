# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        min = 0
        max = len(nums)-1
        while(min <= max):
            mid = min + (max-min)//2

            if target == nums[mid]:
                return mid

            if nums[mid] < target:
                min = mid + 1
            else:
                max = mid - 1
        return min
        