'''
Two Sum II

Given a 1-indexed array of integers numbers that is already 
  sorted in non-decreasing order, find two numbers such that they 
  add up to a specific target number. Let these two numbers be 
  numbers[index1] and numbers[index2] 
  where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by 
  one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. 
  You may not use the same element twice.

Your solution must use only constant extra space. 

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
'''

# Time Complexity: O(n)
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # Setup two pointers (one at the beginning and end of the list)
        i, j = 0, len(numbers) - 1
        
        # Since the list is ordered, we know that if the total or list[i] + list[j]
        #   is greater than the target -> we need to move the right pointer to the left
        #   if the total is less than the target -> move the left pointer to the right
        while i <= j:
            total = numbers[i] + numbers[j]
            if total == target:
                return [i + 1, j + 1]
            elif total > target:
                j -= 1
            else: 
                i += 1