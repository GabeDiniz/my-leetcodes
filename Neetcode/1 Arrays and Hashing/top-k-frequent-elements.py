'''
Top K Frequent Elements

Questions: Given an integer array nums and an integer k, 
  return the k most frequent elements. You may return the 
  answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
'''

# Time Complexity: Worse case -> O(2n) which belongs to O(n) 
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashMap = {}
        for num in nums:
            # If the number exists in the Hashmap, add 1
            if num in hashMap:
                hashMap[num] +=1
            # If the number does no exist, set it to 1
            else:
                hashMap[num] = 1
        # Sort hashMap from greatest to least in terms of occurrences
        #   then return the k most frequent
        sort_hash = sorted(hashMap, key=hashMap.get, reverse=True)
        return sort_hash[:k]