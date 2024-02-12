'''
Majority Element

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
  You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]

Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

class Solution:
  def majorityElement(self, nums: list[int]) -> int:
    # Time Complexity: O(n)
    minimum = (len(nums)//2)
    hashMap = dict(int)
    # Use a hash to keep track of how many times a number has appeared
    for num in nums:
      hashMap[num] += 1
      # If the number appears more than n//2 times -> return the number
      if hashMap[num] > minimum:
        return num