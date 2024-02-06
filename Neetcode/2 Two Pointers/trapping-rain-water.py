'''
Trapping Rain Water

Given n non-negative integers representing an elevation map where the 
  width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
  In this case, 6 units of rain water are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
'''

class Solution:
  def trap(self, height: list[int]) -> int:
    # Time Complexity: O(n)
    n = len(height)

    # Initialize left and right: stores the left and right of each bar
    left = [0] * n
    right = [0] * n
    answer = 0
    left_max, right_max = 0, 0

    # Iterate from left to right to populate left array
    for i in range(n):
      left[i] = left_max
      if left_max < height[i]:
        left_max = height[i]
    
    # Iterate from right to left to populate right array
    for i in range(n - 1, -1, -1):
      right[i] = right_max
      if right_max < height[i]:
        right_max = height[i]
    
    # Iterate through array to calculate the amount of water trapped
    for i in range(n):
      # Calculate the trapped water at each position
      trapped = min(left[i], right[i]) - height[i]
      if trapped > 0:
        answer += trapped
    return answer