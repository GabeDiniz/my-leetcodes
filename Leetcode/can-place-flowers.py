'''
Can Place Flowers

You have a long flowerbed in which some of the plots are planted, 
  and some are not. However, flowers cannot be planted in adjacent plots.

  Given an integer array flowerbed containing 0's and 1's, where 0 means 
  empty and 1 means not empty, and an integer n, return true if n new flowers 
  can be planted in the flowerbed without violating the no-adjacent-flowers 
  rule and false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 
Constraints:
1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
'''

class Solution:
  def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
    # First Solution
    # Time Complexity: O(n)
    # Base case
    if n == 0:
      return True

    for index, pot in enumerate(flowerbed):
      if pot == 0:
        # Default left and right to 0 in current value is first
        #   value or the last value
        #   Do this to avoid list index out of range
        left, right = 0, 0
        if index < len(flowerbed) - 1:
          left = flowerbed[index + 1]
        if index > 0:
          right = flowerbed[index - 1]
        
        # If current pot is surrounded by empty pots -> valid 
        #   plot -> update flowerbed and n
        if left == 0 and right == 0:
          flowerbed[index] = 1
          n -= 1

        if n == 0:
          return True