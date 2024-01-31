'''
Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, 
  return an array answer such that answer[i] is the number of days you 
  have to wait after the ith day to get a warmer temperature. 
  If there is no future day for which this is possible, 
  keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
'''

class Solution:
  def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
    # Time Complexity: O(n)
    # Monotonic Decreasing Stack -> meaning decreasing order by temperature
    stack = []  # Format: [temperature, index]
    answer = [0] * len(temperatures)

    for index, temp in enumerate(temperatures):
      # While stack is not empty and current temp is
      #   greater than top of stack temperature (which also
      #   happens to be the highest temp in the stack)
      while stack and temp > stack[-1][0]:
        top_of_stack = stack.pop()
        i = top_of_stack[1]     # Holds the index
        # Answer is the difference in index positions
        answer[i] = index - i
      # Append current number to the stack
      stack.append([temp, index])
    return answer