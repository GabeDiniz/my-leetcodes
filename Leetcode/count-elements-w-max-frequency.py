'''
Count Elements With Maximum Frequency

You are given an array nums consisting of positive integers.
  
  Return the total frequencies of elements in nums such that those 
  elements all have the maximum frequency.

  The frequency of an element is the number of occurrences of that 
  element in the array.

Example 1:
Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum 
  frequency in the array. So the number of elements in the array with 
  maximum frequency is 4.

Example 2:
Input: nums = [1,2,3,4,5]
Output: 5
Explanation: All elements of the array have a frequency of 1 which is the 
  maximum. So the number of elements in the array with maximum frequency is 5.
'''
from collections import defaultdict

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
      # Time Complexity: O(n)
      hashMap = defaultdict(int)

      # Calculate frequency of each number
      for num in nums:
        hashMap[num] += 1

      # Retrieve the maximum frequency number
      max_val = max(hashMap.values())
      result = 0
      # Iterate through the total frequencies of the elements and
      #   calculate the sum of the numbers that have the max frequency
      for num in hashMap.values():
        if num == max_val:
          result += num

      return result