'''
Container with Most Water

You are given an integer array height of length n. There are n 
  vertical lines drawn such that the two endpoints of the ith 
  line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
  such that the container contains the most water.

Return the maximum amount of water a container can store.
  Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
  In this case, the max area of water the container can contain is 49.
  That's because the max area is generated from 8 (left) and 7 (right). 

  The container can't hold above 7 since it will overflow. Thus, the height is 7.
  The width is also 7 since the left (8) is in position 1 and right (7) is in position 8.
  To get the width, you can do 8 - 1 (or left-index - right-index). 

Example 2:
Input: height = [1,1]
Output: 1
'''

class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Time Complexity: O(n)
        # Init left/right/answer
        left, right, answer = 0, len(height) - 1, 0

        # Iterate through list until left and right pointer crosses
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            answer = max(answer, area)

            # Move the shorter pointer inward (i.e., if height of left is 2 and height of right is
            #   5 -> Move left pointer inward)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return answer

        # Solution 1: O(n^2) - TOO SLOW
        max = 0
        # Left vertical line
        for l in range(len(height)):
            # Right vertical line
            for r in range(l + 1, len(height)):
                left = height[l]    # left number
                right = height[r]   # right number
                width = r - l       # width (right-index - left-index)
                area = min(left, right) * width
                if area > max:
                    max = area
        return max