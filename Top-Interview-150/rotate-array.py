'''
Rotate Array

Link: https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
  def rotate(self, nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # Use a hashMap to store the index:num pair
    hashMap = {}
    # Parse through nums, adding k to the current index.
    # If the new index ends up being large than len(nums), the number
    #   needs to go to the beginning of the list. We can obtain this new
    #   index by taking the remainder of new-index % len(nums).
    # Example: [1] k = 3
    #   The new-index would be 3 because 0 + 3. This is over len(nums) 
    #   so we take the remainder of 3/1, which is 0. New-index = 0. 
    for i in range(len(nums)):
      # Rotate current to the right
      index = i + k
      if index >= len(nums):
        index = index % len(nums)
      hashMap[index] = nums[i]
        
    # Use the hashMap to update nums
    for key in hashMap.keys():
      nums[key] = hashMap.get(key)