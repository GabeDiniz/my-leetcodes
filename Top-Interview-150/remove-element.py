'''
Remove Element

Link: https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
  def removeElement(self, nums: list[int], val: int) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)
    pos = 0
    for num in nums:
      # Shift nums left if they are not equal to val
      if num != val:
        nums[pos] = num
        pos += 1

    return pos