'''
Rearrange Array Elements by Sign

You are given a 0-indexed integer array nums of even length consisting of an 
  equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows 
  the given conditions:

  1. Every consecutive pair of integers have opposite signs.
  2. For all integers with the same sign, the order in which they were present in 
      nums is preserved.
  3. The rearranged array begins with a positive integer.

  Return the modified array after rearranging the elements to satisfy the 
    aforementioned conditions.

Example 1:
Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
  The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
  Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are 
  incorrect because they do not satisfy one or more conditions.  

Example 2:
Input: nums = [-1,1]
Output: [1,-1]
Explanation:
1 is the only positive integer and -1 the only negative integer in nums.
So nums is rearranged to [1,-1].
'''

class Solution:
  def rearrangeArray(self, nums: list[int]) -> list[int]:
    # Second solution
    # Time Complexity: O(n)
    # Space Complexity: O(n) to store answer
    pi, ni, answer = 0, 1, [0]*len(nums)
    for num in nums:
      if num > 0:   # Positive num
        answer[pi] = num
        pi += 2
      else:   # Negative num
        answer[ni] = num
        ni += 2

    return answer
  
    # First solution
    # Time Complexity: O(n)
    # Space Complexity: O(n) to store negatives and positives
    pos, neg = [], []
    
    # Divide positve and negative
    for n in nums:
      if n > 0: 
        pos.append(n)
      else: neg.append(n)

    # Step by 2, update numbers 2 at a time
    for i in range(0, len(nums), 2):
      # Even index -> append pos
      nums[i] = pos[0]
      nums[i + 1] = neg[0]
      pos = pos[1:]
      neg = neg[1:]
    return nums