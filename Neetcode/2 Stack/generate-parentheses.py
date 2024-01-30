'''
Generate Parentheses

Given n pairs of parentheses, write a function to 
  generate all combinations of well-formed parentheses.
 
Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
'''

class Solution:
  def generateParenthesis(self, n: int) -> list[str]:
    def generate(current, opn, close):
      # If length of current parentheses is 2 * n (meaning the current set
      #  of parentheses is complete) -> append it to the result
      if len(current) == 2 * n:
        result.append(current)
        return
      # If number of open brackets is < n then -> recurse through
      #  generate with a new open bracket 
      if opn < n:
        generate(current + '(', opn + 1, close)
      # If number of close brackets is < the number of open brackets 
      #  then -> recurse through generate with a new close bracket 
      if close < opn:
        generate(current + ')', opn, close + 1)
    
    result = []
    generate('', 0, 0)
    return result
  
  '''
  Solution Visualization:
            n = 2
             (0, 0, '')
                  |	
             (1, 0, '(')  
            /           \
      (2, 0, '((')      (1, 1, '()')
          /                 \
    (2, 1, '(()')           (2, 1, '()(')
        /                       \
  (2, 2, '(())')                (2, 2, '()()')
          |	                             |
  res.append('(())')             res.append('()()')
  '''