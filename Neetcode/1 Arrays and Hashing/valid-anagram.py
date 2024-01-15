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

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths don't match -> not an anagram -> return False
        if len(s) != len(t):
            return False

        # For each character in s, remove that character from t
        for char in s:
            if char in t:
                t.replace(char, "")
            # If the corresponding character in s is NOT in t -> return False
            else: 
                return False
        return True