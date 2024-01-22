'''
3-Sum

Given an integer array nums, return all the triplets 
  [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
  and nums[i] + nums[j] + nums[k] == 0.

  Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
  Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()

        # 1: Split the numbers into positives, negatives, and zeros
        negatives, zeros, positives = [], [], []
        for num in nums:
            if num < 0:
                negatives.append(num)
            elif num > 0:
                positives.append(num)
            else:
                zeros.append(num)
        
        # 2: Create a set for negatives and positives to setup O(1) look-up times
        NEGATIVES, POSITIVES = set(negatives), set(positives)

        # Handle 0s cases
        # 3.1: If there is a 0 in the list, add all cases where -num, num exists in NEGATIVES, POSITIVES
        #   i.e., (-3, 0, 3) = 0
        if zeros:
            for num in POSITIVES:
                if -1 * num in NEGATIVES:   # Check if the (-) of num is in NEGATIVES
                    result.add((-1 * num, 0, num))
        # 3.2: If there are 3 zeros in the list, include (0, 0, 0)
        if len(zeros) >= 3:
            result.add((0, 0, 0))
        
        # 4: For all negative pairs, check for their positive compliment
        #   i.e., (-5, -1) -> (6)
        for i in range(len(negatives)):     # iterate through every pair
            for j in range(i + 1, len(negatives)):
                target = -1 * (negatives[i] + negatives[j])
                if target in POSITIVES:
                    # If it exists -> add triple -> [-5, -1, 6]
                    result.add(tuple(sorted([negatives[i], negatives[j], target]))) 

        # 5: Now, for all the positive pairs, check for the negative compliment
        for i in range(len(positives)):
            for j in range(i + 1, len(positives)):
                target = -1 * (positives[i] + positives[j])
                if target in NEGATIVES:
                    result.add(tuple(sorted([positives[i], positives[j], target])))

        return result