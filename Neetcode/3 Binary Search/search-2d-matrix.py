'''
Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

  Each row is sorted in non-decreasing order.
  The first integer of each row is greater than the last integer of the previous row.
  Given an integer target, return true if target is in matrix or false otherwise.

  You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''

class Solution:
  def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
    # Time Complexity: O(log(m * n))
    top, bottom, row = 0, len(matrix) - 1, []  
    left, right = 0, len(matrix[0]) - 1 # left column and right column

    # Find row
    # for i, row in enumerate(matrix):
    while top <= bottom:
      middle = (top + bottom) // 2
      # If the row's left bound is < target and right bound is > target
      #   we have found our row -> break loop
      if matrix[middle][left] <= target and matrix[middle][right] >= target:
        row = matrix[middle]
        break
      elif matrix[middle][left] > target:
        bottom = middle - 1
      elif matrix[middle][right] < target:
        top = middle + 1
    # If the row is still its default value (empty), the target is not present
    if not row: return False

    # Row is now the list that should contain our target
    # Perform binary search on that row
    while left <= right:
      middle = (left + right) // 2
      # If the middle number is < target -> move left pointer
      if row[middle] < target:
        left = middle + 1
      # If the middle number is > target -> move right pointer
      elif row[middle] > target:
        right = middle - 1
      else: 
          return True
    return False