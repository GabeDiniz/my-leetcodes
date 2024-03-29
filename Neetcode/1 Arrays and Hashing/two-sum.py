'''
Two-sum

Question: Given an array of integers nums and 
  an integer target, return indices of the two 
  numbers such that they add up to target.

  You may assume that each input would have exactly 
  one solution, and you may not use the same element twice.

  You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
'''

# Time Complexity: O(n)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap = {}
        for i, num in enumerate(nums):
            # Missing number is not in Hashmap
            # Append current number, index
            if hashMap.get(target - num) is None:
                hashMap[num] = i
            else:
                # Missing number exists, return it:
                return [i, hashMap[target-num]]

    # Time Complexity: O(n^2)       
    def slowTwoSum(self, nums: list[int], target: int) -> list[int]:
        result = []

        for i in range(len(nums) - 1):
            for x in range(1, len(nums)):
                if nums[i] + nums[x] == target:
                    result.append(i)
                    result.append(x)
                    return result
