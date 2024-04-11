'''
Merge Sorted Array

Link: https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
  def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # Time Complexity: O(m + n)
    # Space Complexity: O(1)

    # Initialize values where...
    # i = right index of nums1
    # j = right index of nums2
    # write_index = current index to write to starting from the right
    i, j, write_index = m - 1, n - 1, m + n - 1
    
    # Run loop while while j >= 0 (i.e., while nums2 still has numbers in it)
    #   Explanation: nums1 is already in order, therefore, if j (nums2) has nothing
    #       left to be added, then nums1 is complete and the lists are merged. 
    while j >= 0:
      if i >= 0 and nums1[i] > nums2[j]:
        nums1[write_index] = nums1[i]
        i -= 1
      else:
        nums1[write_index] = nums2[j]
        j -= 1
      write_index -= 1