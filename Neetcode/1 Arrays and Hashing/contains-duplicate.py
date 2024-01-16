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

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # First Solution
        # Time Complexity: O(n)
        '''
        # Store duplicates
        dups = []

        # Iterate through list of nums
        for num in nums:
            # If the num is already in dups -> a duplicate exists -> return True
            if num in dups:
                return True
            # Append the num to the dups list
            dups.append(num)
        return False
        '''
        # Improved solution
        # Time Complexity: O(1) 
        dupSet = set()

        for num in nums:
            if num in dupSet:
                return True
            dupSet.add(num)
        return False