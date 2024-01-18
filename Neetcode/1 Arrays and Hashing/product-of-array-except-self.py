'''
Product of Array Except Self

Questions: Given an integer array nums, return an array answer such that 
  answer[i] is equal to the product of all the elements of nums except nums[i].

  The product of any prefix or suffix of nums is guaranteed to 
  fit in a 32-bit integer.

  You must write an algorithm that runs in O(n) time and without 
  using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

# Time Complexity: O(n)
# O(1) Space Complexity 
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = [0] * (len(nums))
        
        # Prefix
        # Calculate the prefix product as you move right to left
        #   Example: prefix product of [2, 4, 5, 10] -> [1, 2, 8, 40]
        prefix = 1
        for i in range(len(nums)):    
            answer[i] = prefix
            prefix *= nums[i]

        # Suffix
        # Calculate the suffix product as you move right to left
        #   and multiply it by the respective suffix to determine
        #   the product of array except self
        #   Example: suffix product of [2, 4, 5, 10] -> [200, 50, 10, 1]
        #       Instead of doing an intermediate step, we can multiply that
        #       by the suffix to get the answer for each position
        #   Example: With the prefix product being - [1, 2, 8, 40]
        #       the suffix calculates 40*suffix (40 * 1) ->
        #       8*suffix (8 * 10) -> 2*suffix (2 * 50) -> 1*suffix (1 * 200)
        suffix = 1
        for n in range(len(nums) - 1, -1, -1):
            answer[n] *= suffix
            suffix *= nums[n]
        return answer