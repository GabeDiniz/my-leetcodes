'''
Contains Duplicate

Question: Given an integer array nums, return true if 
  any value appears at least twice in the array, and 
  return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false
'''

# Time Complexity: O(n)
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dups = []

        for num in nums:
            if num in dups:
                return True
            dups.append(num)
        return False