'''
GRoup Anagrams

Questions: Given an array of strings strs, group the 
  anagrams together. You can return the answer in any order.

  An Anagram is a word or phrase formed by rearranging the 
  letters of a different word or phrase, typically using all 
  the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
'''
from collections import defaultdict

# Time Complexity O(n)
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashMap = {}    # Example: {"aet": ["eat", "ate"], "ant": [], "abt": []}
        
        # First solution: 
        '''
        for word in strs:
            # Sort characters:
            curr = ''.join(sorted(word))
            # If sorted characters exists, append it
            if curr in hashMap:
                newList = hashMap[curr]
                newList.append(word)
            # If sorted characters doesn't exist, create it and append it
            else:
                hashMap[curr] = [word]
        '''
        
        hashMap = defaultdict(list)
        
        # Better Way:
        for word in strs:
            sorted_word = ''.join(sorted(word))
            hashMap[sorted_word].append(word)
        
        return list(hashMap.values())