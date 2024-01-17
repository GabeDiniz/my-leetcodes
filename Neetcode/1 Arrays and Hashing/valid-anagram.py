'''
Valid Anagram

Question: Given two strings s and t, return true if t 
  is an anagram of s, and false otherwise.
Explanation: An Anagram is a word or phrase formed by 
  rearranging the letters of a different word or phrase, 
  typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''

# Time Complexity: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort both strings. If they are the same they are a
        #   valid anagram. 
        sort_s = sorted(s)
        sort_t = sorted(t)
        return sort_s == sort_t