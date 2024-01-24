'''
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
  determine if the input string is valid.
  An input string is valid if:

Open brackets must be closed by the same type of brackets.
  Open brackets must be closed in the correct order.
  Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''

class Solution:
    def isValid(self, s: str) -> bool:
        # Time Complexity: O(n)
        brackets = {'{': '}','(': ')','[': ']'}
        i = 0
        stack = []
        # Base case
        if len(s) < 2:
            return False
        
        # Iterate through each bracket
        for char in s:
            # If its an open bracket (i.e., in dictionary: brackets)
            #   append its corresponding closing bracket to the stack
            if char in brackets:
                stack.append(brackets[char])
            # Elif the stack is not empty AND the top most element of the
            #   stack (the closing bracket to the last open brack) is equal
            #   to the current char -> pop the element and continue 
            elif len(stack) != 0 and stack.pop() == char: continue
            else: return False

        # If the stack still has brackets inside -> a bracket was not closed, return False
        if len(stack) > 0:
            return False
        return True