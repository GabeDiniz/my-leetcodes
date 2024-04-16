'''
Remove Duplicates from Sorted Array

Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
  def removeDuplicates(self, nums: list[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)

    # Use set to keep track of unique values
    hashSet = set()
    index = 0
    for num in nums:
      if num not in hashSet:
        nums[index] = num
        hashSet.add(num)
        index += 1
    # Return the length of unique values
    return len(hashSet)