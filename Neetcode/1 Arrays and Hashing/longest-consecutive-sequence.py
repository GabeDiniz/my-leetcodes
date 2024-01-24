'''
Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of 
  the longest consecutive elements sequence.
  You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Solution 1: O(n log n)
        # Handle base case of length being 0, or 1
        if len(nums) < 2: return len(nums)
        
        # Init variables
        ans, cur = 1, 1
        seq = set()

        # Create a set to remove duplicates: O(n)
        for num in nums:
            seq.add(num)
        seq = sorted(seq)   # Sort set: O(nlogn)
        
        for i in range(1, len(seq)):  # O(n)
            # Check if next num is part of the sequence
            #   (i.e., if previous + 1 == current)
            if seq[i - 1] + 1 == seq[i]:
                cur += 1
            # Else reset cur
            else: cur = 1

            ans = max(cur, ans)
        return ans