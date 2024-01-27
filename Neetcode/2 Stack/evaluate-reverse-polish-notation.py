'''
Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents an arithmetic expression 
  in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
  The valid operators are '+', '-', '*', and '/'.
  Each operand may be an integer or another expression.
  The division between two integers always truncates toward zero.
  There will not be any division by zero.
  The input represents a valid arithmetic expression in a reverse polish notation.
  The answer and all the intermediate calculations can be represented in a 32-bit integer.
 
Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
'''

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # Time Complexity: O(n)
        stack = []
        operators = "+-*/"

        # Loop through each token, adding and removing from the stack 
        #   accordingly. At the end of the loop, the 1 number left in 
        #   the stack is the answer
        for token in tokens:
            # When token is an operator -> pop out the last 2 items in the stack
            #   and handle the case according to operator
            if token in operators:
                val1 = stack.pop()
                val2 = stack.pop()
                if token == "+":
                    stack.append(val1 + val2)
                elif token == "-":
                    stack.append(val2 - val1)
                elif token == "*":
                    stack.append(val1 * val2)
                elif token == "/":
                    stack.append(int(val2 / val1))
            # Otherwise token is an integer -> add int to the stack
            else:
                stack.append(int(token))
        return stack.pop()