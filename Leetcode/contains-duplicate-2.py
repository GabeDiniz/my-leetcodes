'''
Contains Duplicate

Question: Given an integer array nums and an 
  integer k, return true if there are two distinct 
  indices i and j in the array such that 
  nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # Solution 3: Best solution
        # Time Complexity: O(n) slightly faster than solution 2
        hashMap = {}    # {num: index, 1: 0, 5: 1, 10: 2}
        for i, num in enumerate(nums):
            if num in hashMap and i - hashMap[num] <= k: 
                return True
            hashMap[num] = i
        return False

        # Solution 2: 
        # Time Complexity: O(n)
        hashMap = defaultdict(int)
        window = nums[0:k + 1]
        # Create a Hashmap of the initial window based on k
        for num in window:
            hashMap[num] += 1
            if hashMap[num] > 1:
                return True

        # Update the left of the window (the number to the left that
        #   is no longer in the window) and update the Hashmap to reflect
        #   the new number that has entered the window. 
        left = 0
        for num in nums[k + 1:]:
            hashMap[nums[left]] -= 1
            if hashMap[num] == 0:
                hashMap[num] += 1
            elif hashMap[num] == 1:
                return True
            left += 1
        
        # Solution 1:
        # Time Complexity: O(n*k)        
        for i, num in enumerate(nums):
            sublist = nums[i + 1:i + k + 1]
            if num in sublist:
                return True
        return False
    