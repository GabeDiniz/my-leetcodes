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
        result = []
        for num in nums:
            # If the number exists in the Hashmap, add 1
            if num in hashMap:
                hashMap[num] +=1
            # If the number does no exist, set it to 1
            else:
                hashMap[num] = 1
        # For each number that appeared above, check if the value
        #   is >= k (i.e., the number appeared a minimum of k times)
        #   If it did -> append it to our result. 
        for key in hashMap.keys():
            if hashMap[key] >= k:
                result.append(key)
        return result