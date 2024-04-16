'''
Remove Duplicates from Sorted Array II

Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
  def removeDuplicates(self, nums: list[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)
      
    index = 1   # pointer used to move elements in the array to ensure no element appears > 2
    frequency = 1 # pointer to keep track of how many times the current number has appeared

    # Explanation: Increase the number frequency by checking the current numbers with the one before. 
    #   If the number is the same, frequency + 1. Otherwise, its a new number and we reset it to 1. 
    # If the frequency is <= 2, we copy the current number and move it to position index. 
    for i in range(1, len(nums)):
      if nums[i] == nums[i - 1]:
        frequency += 1
      else:
        frequency = 1

      if frequency <= 2:
        nums[index] = nums[i]
        index += 1
    return index