'''
Least Number of Unique Integers after K Removals

Given an array of integers arr and an integer k. Find the least number of 
  unique integers after removing exactly k elements.

Example 1:
Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.

Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
'''

from collections import Counter

class Solution:
  def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)
    
    # Map the frequency
    frequency = Counter(arr)
    # Sort the frequency as a num-frequency set (i.e., [(3, 2), (2, 4), ...] )
    sorted_frequency = sorted(frequency.items(), key = lambda x: x[1])
    
    # Go through the sorted num-frequency pair, removing the least frequent
    #   until removing k from frequency does not remove the number
    for num, freq in sorted_frequency:
      if k >= freq:
        k -= freq # subtract that numbers frequency
        del frequency[num] # remove the number from the frequency_map
      else: break
    return len(frequency)