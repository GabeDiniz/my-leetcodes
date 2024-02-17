'''
Binary Search

Given an array of integers nums which is sorted in ascending order, and an 
  integer target, write a function to search target in nums. If target exists, 
  then return its index. Otherwise, return -1.

  You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''

class Solution:
  def search(self, nums: list[int], target: int) -> int:
    # Time Complexity: O(log n)

    # Init left and right index values
    left, right = 0, len(nums)-1

    while left <= right:
      # Retrieve the middle point index
      middle = (left + right) // 2
      # If the middle number is < target -> move left pointer
      if nums[middle] < target:
        left = middle + 1
      # If the middle number is > target -> move right pointer
      elif nums[middle] > target:
        right = middle - 1
      # Otherwise, the target was found -> return middle
      else: 
        return middle
    return -1